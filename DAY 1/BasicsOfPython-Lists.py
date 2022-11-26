#This is a Comment
#Basic Hello World Code

msg="Hello World!";
print(msg);

name="Nikhil";

print(msg+", "+name);

#Creating an List of Movie Names

movies=["ZNMD", "RNBDJ", "DDLJ", "3KG"];

#Lists are like arrays, hence here we are creating a list of Strings, but python doesn't need the type of an identifier, it only needs to understand that its an list, with [].

#Accessing the List.
#We can use index for that process, list starts with index 0, that means first elemnt of list will be stored in 0 index, second elemnt in 1st index and so on.

firstElement=movies[0];
print(firstElement);

secondElement=movies[1];
print(secondElement);

#Getting list Length.

lengthOfList=len(movies);
print(lengthOfList);

#With your list created, you can use list methods to add a single data item to the end of your list (using the append() method), remove data from the end of your list (with the pop() method), and add a collection of data items to the end of your list

movies.append("Gravity");
print(movies);
movies.pop();
print(movies);
movies.extend(["Interstellar", "Thor"]);
print(movies);

#Finally, find and remove a specific data item from your list (with the remove() method) and then add a data item before a specific slot location (using the insert() method):

movies.remove("Thor");
print(movies);

movies.insert(0, "Ham Tum");
print(movies);

#You can create Python Lists with multiple types of data like int, strings together for example.
#inserting ratings for each movie
movies.insert(1,5);
movies.insert(3,4.4);
movies.insert(5,3);
movies.insert(7,5);
movies.insert(9,4.8);
movies.insert(11,5);

print(movies);

#Traversing the lists using the loops
#1. using for loop.

# for movie in movies:
#     print(movie);

#2. Using While loop

count=0;
while(count<len(movies)):
    print(movies[count])
    count=count+1;

#list inside a list

movieWithActors=["ZNMD",5,["Farhan", 40],["Hritik",45]];
#To Access Farhan's Age
farhansAge=movieWithActors[2][1]; #output should come 40 #Second List starts at index 2 and age is at index 1 of that list
print(farhansAge);
