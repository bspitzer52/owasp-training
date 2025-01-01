from scrapy.cmdline import execute
import sys
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="XSS Scrapy scanner")
    parser.add_argument('-u', '--url', help="URL to scan; -u http://example.com", required=True)
    parser.add_argument('-l', '--login', help="Login name; -l username")
    parser.add_argument('-p', '--password', help="Password; -p password")
    parser.add_argument('-c', '--connections', default='30', help="Max simultaneous connections (default=30)")
    parser.add_argument('-r', '--ratelimit', default='0', help="Rate limit (requests per minute)")
    parser.add_argument('--basic', help="Use HTTP Basic Auth to login", action="store_true")
    parser.add_argument('-k', '--cookie', help="Cookie key (e.g., SessionID=afgh3193)")
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    rate = args.ratelimit
    if rate not in [None, '0']:
        rate = str(60 / float(rate))
    try:
        cookie_key = args.cookie.split('=',1)[0] if args.cookie else None
        cookie_value = ''.join(args.cookie.split('=',1)[1:]) if args.cookie else None
        execute([
            'scrapy', 'crawl', 'xsscrapy',
            '-a', f'url={args.url}',
            '-a', f'user={args.login}',
            '-a', f'pw={args.password}',
            '-a', f'basic={args.basic}',
            '-a', f'cookie_key={cookie_key}',
            '-a', f'cookie_value={cookie_value}',
            '-s', f'CONCURRENT_REQUESTS={args.connections}',
            '-s', f'DOWNLOAD_DELAY={rate}'
        ])
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
