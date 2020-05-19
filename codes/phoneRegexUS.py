#! python3

import re, pyperclip

text = pyperclip.paste()

phoneRegex = re.compile(r'''(
                        \(?(\+88)?\)?
                        (\s|-)?
                        01
                        \d
                        \s?
                        \d
                        \s?
                        \d{3,4}
                        \s?
                        \d{3,4}
                        (\s*(ext|x|ext.)?\s*\d{2,5})?
                        )''', re.VERBOSE)

mo = phoneRegex.findall(text)

for i in range(len(mo)):
    print('Number-' + str(i+1) + ': '+ mo[i][0])

'''01682002444,
+8801682002444,
(+88) 0168 2002 444,
(+88) 0168 200 2444,
(+88) 016 8200 2444,
(+88) 016 8200 2444 0000'''
