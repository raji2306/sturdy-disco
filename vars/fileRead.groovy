def fileRead(string filename){
  def file = new File(filename)
  if(file.exists()){
    def content = file.readLines() 
  }
   else {
     echo "File doesn't exist, So can't able to read the file"
   }
}
