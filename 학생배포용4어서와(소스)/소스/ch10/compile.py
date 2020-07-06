
#에러발생
with open('.//ch10//mymodule.py') as f:
     lines = f.read()

code_obj = compile(lines, './/ch10//mymodule.py', 'exec')
exec(code_obj)
