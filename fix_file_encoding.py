input_str = '''
makejdsp.vc6
makerdsp.vc6
makermak.vc6
maketdep.vc6
maketdsp.vc6
makewdsp.vc6
makewmak.vc6
'''

lines = input_str.splitlines()
lines = list(map(lambda x: x.strip(), lines))
lines = list(filter(lambda x: len(x) > 0, lines))

todo_filepath_list = lines
# print(todo_filepath_list)
print('len(todo_filepath_list)', len(todo_filepath_list))

for todo_filepath in todo_filepath_list:
    print(todo_filepath)
    bs = open(todo_filepath, 'rb').read()
    content_str = bs.decode('cp852')
    open(todo_filepath, 'wb').write(content_str.encode('utf-8'))
