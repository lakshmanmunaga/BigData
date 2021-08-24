import io
def load_properties(filepath, sep='=', comment_char='#'):

 props={}
 with open(filepath,'r') as f:
    for line in f:
         l = line.strip()

         if l and not l.startswith(comment_char):
                key_value = l.split(sep)
                key = key_value[0].strip()
                value = sep.join(key_value[1:]).strip().strip('"')
                props[key] = value

    print(props['path'])
    print(props['head_count'])
load_properties(filepath='configue.ini')
