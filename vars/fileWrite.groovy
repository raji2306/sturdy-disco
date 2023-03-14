def fileWrite(string filename){
  def file = new File(filename)
  def writer = new FileWriter(file, true)
    if(writer.canRead()){ 
      writer.write("Hello, Everything will be alright. Be calm")
      writer.close()
    }  
    else {
      println "Sorry, The requested file is not writable"
}
