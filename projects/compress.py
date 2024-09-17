import gzip
input_file="D:/input.txt"
output_file="compressed.gz"
with open(input_file,"rb") as f ,gzip.open(output_file,"wb") as f_out:
    f_out.writelines(f)
print(f'{input_file} compresed to {output_file}')