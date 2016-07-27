html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>title of the code</title>
</head>
<body>
```
for i in range(10):
    print "<td>hello world in this tornament</td>"

for i in range(19):
    print "hello world"
```
hello
```
print "<td html >"

```

```start
<html><b>hello</b></html>
<p>hello world</p>
<a href="hello">arindam</a>
```end

</body>
</html>
"""

from cStringIO import StringIO
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout

def parse_template(html):
    find_code = html.split('```')
    ANS = []
    for i in find_code:
        try:
            a = "".join(compile(i))
            ANS.append(a)
            find_code[find_code.index(i)] = a
        except:
            pass
    # print find_code
    return "".join(ANS)

def compile(code):
    with Capturing() as output:
        exec code
    return output

print parse_template(html)
