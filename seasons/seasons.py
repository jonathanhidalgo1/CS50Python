from datetime import date
import inflect


def main():
    date = input('date: ')
    print(convert(date))
    
def convert(n):
    try:
        p = inflect.engine()
        somedate = date.fromisoformat(n)
        today = date.today()
        math =  today - somedate
        minutes = int(math.total_seconds() / 60)
        
        return f"{p.number_to_words(minutes, andword='')}, minutes"
    
    except ValueError:
        return "invalid date"

if __name__ == "__main__":
    main()
    
    
    