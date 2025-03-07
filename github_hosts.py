import socket
import platform
import os
import shutil
import time
from datetime import datetime

# 配置部分
TARGET_DOMAINS = {
    "github.com": "",
#    "assets-cdn.github.com": "",
    "github.global.ssl.fastly.net": "",
    "raw.githubusercontent.com": ""  # 新增常见加速域名
}
HOSTS_PATHS = {
    "Windows": r"C:\Windows\System32\drivers\etc\hosts",
    "Linux": "/etc/hosts",
    "Darwin": "/etc/hosts"
}
DNS_SERVER = "114.114.114.114"  # 使用 Google DNS 查询

def is_admin():
    """检查管理员权限"""
    try:
        return os.getuid() == 0  # Unix
    except AttributeError:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0  # Windows

def get_clean_ip(domain):
    """使用指定 DNS 查询解析 IP"""
    try:
        # 创建 UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((DNS_SERVER, 53))
        
        # 构建 DNS 查询数据包
        query = socket.gethostbyname(domain)
        return query
    except Exception as e:
        print(f"无法解析 {domain}: {str(e)}")
        return None

def backup_hosts(hosts_path):
    """创建带时间戳的备份"""
    backup_path = f"{hosts_path}.bak.{datetime.now().strftime('%Y%m%d%H%M%S')}"
    shutil.copy(hosts_path, backup_path)
    return backup_path

def modify_hosts(hosts_path, ip_map):
    """修改 hosts 文件"""
    new_lines = []
    found_existing = False
    
    with open(hosts_path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line_strip = line.strip()
            
            # 保留注释和空行
            if line.startswith("#") or not line_strip:
                new_lines.append(line)
                continue
                
            # 检查现有 GitHub 条目
            parts = line.split()
            if len(parts) < 2:
                new_lines.append(line)
                continue
                
            current_ip, current_domain = parts[0], parts[1]
            if current_domain in ip_map:
                if not found_existing:
                    new_lines.append(f"# === GitHub加速开始 ({datetime.now()}) ===\n")
                    found_existing = True
                continue  # 跳过旧条目
                
            new_lines.append(line)

    # 添加新条目
    if not found_existing:
        new_lines.append(f"\n# === GitHub加速开始 ({datetime.now()}) ===\n")
        
    for domain, ip in ip_map.items():
        new_lines.append(f"{ip}\t{domain}\n")
        
    new_lines.append(f"# === GitHub加速结束 ===\n\n")
    
    # 写入新内容
    with open(hosts_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

def flush_dns():
    """刷新 DNS 缓存"""
    system = platform.system()
    if system == "Windows":
        os.system("ipconfig /flushdns")
    elif system == "Darwin":
        os.system("sudo killall -HUP mDNSResponder")
    elif system == "Linux":
        os.system("systemctl restart systemd-resolved")

def main():
    # 检查权限
    if not is_admin():
        print("请以管理员/root权限运行此脚本！")
        if platform.system() == "Windows":
            print("尝试重新请求权限...")
            import ctypes
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return

    # 获取系统类型
    system = platform.system()
    hosts_path = HOSTS_PATHS.get(system)
    if not hosts_path:
        print("不支持的操作系统")
        return

    # 解析所有域名
    print("正在查询最新 IP 地址...")
    success = True
    for domain in TARGET_DOMAINS:
        ip = get_clean_ip(domain)
        if not ip:
            success = False
            break
        TARGET_DOMAINS[domain] = ip
        
    if not success:
        print("部分域名解析失败，请检查网络连接")
        return

    # 显示变更内容
    print("\n即将修改 hosts 文件，添加以下条目：")
    for domain, ip in TARGET_DOMAINS.items():
        print(f"{ip}\t{domain}")
        
    if input("\n是否继续？(y/n) ").lower() != "y":
        return

    # 备份原文件
    backup_path = backup_hosts(hosts_path)
    print(f"\n已创建备份文件：{backup_path}")

    # 执行修改
    try:
        modify_hosts(hosts_path, TARGET_DOMAINS)
        print("\nHosts 文件修改成功！")
        
        # 刷新 DNS
        print("刷新 DNS 缓存...")
        flush_dns()
        time.sleep(2)
        
    except Exception as e:
        print(f"修改失败: {str(e)}")
        print("正在恢复备份...")
        shutil.copy(backup_path, hosts_path)
        print("已恢复原始 hosts 文件")

if __name__ == "__main__":
    main()