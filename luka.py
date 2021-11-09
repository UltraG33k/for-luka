import glob, re, os

path = r"" # Add the direct path to your folder here

for filename in glob.glob( path + '/*'):
    pattern = r'(\w{13})(\.jpg)'
    replace = r'.jpg'
    new_name = re.sub(pattern, replace, filename)
    print(filename + ' -> ' + new_name)
    os.rename(filename, new_name)
