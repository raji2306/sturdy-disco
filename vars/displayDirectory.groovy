def displayDirectory(String directory){
  def filename = new File(directory)
  if(filename.isDirectory()){
    def files  = filename.listFile()
    files.each {
      file -> println file.getName()
   }
  }
  else {
    println "Not able to located the requested directory, Re-check the Path"
  }
}
