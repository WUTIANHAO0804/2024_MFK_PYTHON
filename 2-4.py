s = input()
start = s.find("'") + 1  
end = s.find("'", start)  
result = s[start:end]    
print(result)            