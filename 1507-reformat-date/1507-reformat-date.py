class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
              "Jan" : 1,
              "Feb" : 2, 
              "Mar" : 3, 
              "Apr" : 4, 
              "May" : 5, 
              "Jun" : 6, 
              "Jul" : 7, 
              "Aug" : 8, 
              "Sep" : 9, 
              "Oct" : 10, 
              "Nov" : 11, 
              "Dec" : 12
        }
        
        d, m, y = date.split()
        d = d[:2] if d[1].isdigit() else "0" + d[:1]
        m = str(months[m])
        m = m if len(m) == 2 else "0" + m
        
        
        return f"{y}-{m}-{d}"
        
            