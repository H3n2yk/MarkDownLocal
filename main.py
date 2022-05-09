 # This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
HeaderAll = r'(  # {%d}\s)(.*)'
BoldItalicText   = r'(\ * | \_) + (\S+)(\ * | \_)+'
LinkText = r'(\[.* \])(\((\w{3, 5})(\:\ / \ /). *\))'
ImageFile = r'(\!)(\[(?:.*)?\])(\(.* (\.(\w{3}))(?:(\s\"|\')(\w|\W|\d)+(\"|\'))?\))'
ImageFileShort = r"(?:\!)(?:\[(.*)?\])(?:\()(.*(?:))(?:\))"
ListText = r'( ^ (\W{1})(\s)(.*)(?:$)?)+'
NumberedListText = r'(^ (\d+\.)(\s)(.*)(?:$)?)+'
BlockQuote = r'(^ (\ > {1})(\s)(.*)(?:$)?)+'
InlineCode = r"(\\'{1})(.*)(\\'{1})"
CodeBlock = r"(\\'{3}\\n+)(.*)(\\n+\\'{3})"
HorizontalLine = r'(\= | \- | \ *){3}'
EmailUrlText = r'(\ < {1})((\S+ @ \S+) | (\w{3, 5}?:\ / \ / (?:www\.| (?!www))[a - zA - Z0 - 9][a - zA - Z0 - 9 -] + [a - zA - Z0 - 9]\.[ ^\s]{2, } | www\.[a - zA - Z0 - 9][a - zA - Z0 - 9 -] + [a - zA - Z0 - 9]\.[ ^\s]{2, } | https?:\ / \ / (?:www\.| (?!www))[a - zA - Z0 - 9] +\.[ ^\s]{2, } | www\.[a - zA - Z0 - 9] +\.[ ^\s]{2, }))(\ > {1})'
QText = r'(\"|\')(\w|\W|\S)+(\"|\')'
TableText = r'(((\ |)([a - zA - Z\d +\s# !@\'\"():;\\\/.\[\]\^<={$}>?(?!-))]+))+(\|))(?:\n)?((\|)(-+))+(\|)(\n)((\|)(\W+|\w+|\S+))+(\|$)'
ThreeUA = '(\_ | \ *) {3}'
TwoUA = '(\_ | \ *){2}'
OneUA = '(\_ | \ *){1}'
Url = r'(https?:\ / \ / (?:www\.| (?!www))[a - zA - Z0 - 9][a - zA - Z0 - 9 -] + [a - zA - Z0 - 9]\.[ ^\s]{2, } | www\.[a - zA - Z0 - 9][a - zA - Z0 - 9 -] + [a - zA - Z0 - 9]\.[ ^\s]{2, } | https?:\ / \ / (?:www\.| (?!www))[a - zA - Z0 - 9] +\.[ ^\s]{2, } | www\.[a - zA - Z0 - 9] +\.[ ^\s]{2, })'
TableSep = r'((\ |)(-+)) + (\ |)(\n)'
UnText = r'(\"|\')(\w|\W|\S)+(\"|\')'

ImageFileShort = r"(?:\!)(?:\[(.*)?\])(?:\()(.*(?:))(?:\))"
pdf = r"(?:\{%pdf\s)(.*)(?:%\})"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
