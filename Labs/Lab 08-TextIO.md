# Programming in Science – Lab 9-TextIO

### Question(s)

1. Read and convert data  
   - Create a `data.csv` file with data `"0,30,45,90"`
   - Write a function `read_file(file_path)` that reads from a file and 
     converts the data into a list of number
   - Write a function `calc_sin(xs)` that takes a list of `x` (degree) values, return the `sin()` value of them
   - Write a function `write_file(xs, sins, file_path)` that takes a list of `x` values, a list of `sin` values and a file path, then write the x values and sin values in the file indicated in the file path, write data as the example shows 
   - Use the first function to read the `data.csv` file, then use the second function to calculate the `sin()` values, then use the third function to write the result into `sin.csv` file 
   
   #### Example:
   ```
   angel,sin()
   0,0
   30,0.5
   45,0.71
   90,1
   ```
