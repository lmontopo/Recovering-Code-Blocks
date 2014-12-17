import re 
import os

all_files = os.listdir(".")
markdown_files = [i for i in all_files if i.endswith(".md")]

print markdown_files


def process_code_block(code_block):
	new_code_block = ['```python\n']
	code_block = code_block[2:-2]
	code = [re.sub(r"^\|.*?\|\s*(.*?)\s*\|$", r'\1', line) for line in code_block]
	code = filter(lambda x: x!='<div class="highlight">\n' and x!='</div>\n', code)
	new_code_block.extend(code)
	new_code_block.append('```\n')
	print new_code_block
	return new_code_block



def process_file(mdfile):
	with open(mdfile) as f, open("output/"+mdfile, 'w') as out:
		inside_code_block = False
		for line in f:
			if re.match(r"\+-+\+-+\+", line):
				if not inside_code_block:
					code_block_lines = []
				else:
					code_block_lines.append(line)
					out.writelines(process_code_block(code_block_lines))
				inside_code_block = not inside_code_block
				continue 
			if not inside_code_block:
				out.write(line)
			else:
				code_block_lines.append(line) 



for mdfile in markdown_files:
	process_file(mdfile)

