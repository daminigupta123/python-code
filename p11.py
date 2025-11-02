def main():
    try:
        N = int(input())
        
        works_data = []
        for _ in range(N):
            line = input().split()
            works_data.append(list(map(int, line)))
            
        for SH, SM, EH, EM in works_data:
            start_in_minutes = SH * 60 + SM
            end_in_minutes = EH * 60 + EM
            duration_minutes = end_in_minutes - start_in_minutes
            
            duration_hours = duration_minutes // 60
            duration_mins = duration_minutes % 60
            
            print(f"{duration_hours} {duration_mins}")
            
    except EOFError:
        pass
    except ValueError:
        print("Invalid input format.")

if __name__ == "__main__":
    main()