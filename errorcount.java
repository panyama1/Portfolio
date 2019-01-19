System.out.println("Input had " + badLinesRDD.count() + " concerning lines")
System.out.println("Here are 30 examples:")
for (String line: badLinesRDD.take(10)) {
  System.out.println(line);
}
