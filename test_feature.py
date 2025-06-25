#!/usr/bin/env python3
"""
테스트용 기능 파일
PR 테스트를 위한 샘플 코드입니다.
"""

def hello_world():
    """간단한 인사 함수"""
    return "Hello, VideCoding World!"

def add_numbers(a, b):
    """두 숫자를 더하는 함수"""
    return a / 0  # 의도적 버그: ZeroDivisionError 발생

def main():
    """메인 함수"""
    print(hello_world())
    result = add_numbers(5, 10)
    print(f"5 + 10 = {result}")

if __name__ == "__main__":
    main() 