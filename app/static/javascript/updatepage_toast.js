function toast(question_id, question_type, question_option) {

    // If first question, say hello to user
    if (question_id == "STUDENT_NAME") {

        // Store user's name in array user_name
        var user_name = $("#STUDENT_NAME").val().split(' ');

        // Toast user's first name
        Materialize.toast("Hello, " + user_name[0] + "!", 3000)
    }

    // If second question, encourage user
    if (question_id == "INSTRUCTOR_NAME") {

        // Store clinical instructor's name in array instructor_name
        var instructor_name = $("#INSTRUCTOR_NAME").val().split(' ');

        // Toast user's first name
        Materialize.toast("Wow! " + instructor_name[0] + " is lucky to have you!", 3000)
    }

    // If third question, encourage user
    if (question_id == "CLIENT_NAME") {

        // Store client's name in array client_name
        var client_name = $("#CLIENT_NAME").val().split(' ');

        // Toast with client's first name
        Materialize.toast("I'm sure " + client_name[0] + " really appreciates your work!", 3000)
    }

    // If fourth question, comment on client's birthday
    if (question_id == "q004") {

        // Store client's birthdate in array client_birthdate
        var client_birthdate = $("#q004textbox").val().split(' ');

        // Create dictionary for year/people
        var famous_birthdates = {
            "1940": "Pele and Bruce Lee",
            "1941": "Bob Dylan and Martha Stewart",
            "1942": "Muhammad Ali and Stephen Hawking",
            "1943": "Mick Jagger and Christopher Walken",
            "1944": "George Lucas and Diana Ross",
            "1945": "Bob Marley and Steve Martin",
            "1946": "Donald Trump and Bill Clinton",
            "1947": "Hilary Clinton and Elton John",
            "1948": "Samuel L. Jackson and George R.R. Martin",
            "1949": "Caitlyn Jenner and Meryl Streep",
            "1950": "Bill Murray and Narendra Modi",
            "1951": "Robin Williams and Ben Carson",
            "1952": "Shigeru Miyamoto and Mr. T",
            "1953": "Tim Allen and Hulk Hogan",
            "1954": "Oprah Winfrey and Denzel Washington",
            "1955": "Bill Gates and Steve Jobs",
            "1956": "Tom Hanks and Theresa May",
            "1957": "Martin Luther King III and Tony Abbott",
            "1958": "Michael Jackson and Ellen DeGeneres",
            "1959": "Magic Johnson and Weird Al Yankovic",
            "1960": "Diego Maradona and Bono",
            "1961": "Barack Obama and Princess Diana",
            "1962": "Jim Carrey and Jerry Rice",
            "1963": "Michael Jordan and Whitney Houston",
            "1964": "Michelle Obama and Sandra Bullock",
            "1965": "Dr. Dre and J.K. Rowling",
            "1966": "Janet Jackson and Mike Tyson",
            "1967": "Will Ferrell and Julia Roberts",
            "1968": "Will Smith and Tony Hawk",
            "1969": "Jay Z and Jennifer Aniston",
            "1970": "Mariah Carey and Ted Cruz",
            "1971": "Snoop Dogg and Tupac Shakur",
            "1972": "Cameron Diaz and Notorious B.I.G.",
            "1973": "Pharell Williams and Tyra Banks",
            "1974": "Jimmy Fallon and Leonardo DiCaprio",
            "1975": "Angelina Jolie and Tiger Woods",
            "1976": "Ronaldo and Reese Witherspoon",
            "1977": "Kanye West and Floyd Mayweather Jr.",
            "1978": "Kobe Bryant and John Legend",
            "1979": "Kevin Hart and Kourtney Kardashian",
            "1980": "Kim Kardashian and TI",
            "1981": "Beyonce Knowles and Alicia Keys",
            "1982": "Dwayne Wade and Eddie Redmayne",
            "1983": "Aaron Rodgers and Amy Winehouse",
            "1984": "Lebron James and Mark Zuckerberg",
            "1985": "Cristiano Ronaldo and Michael Phelps",
            "1986": "Drake and Usain Bolt",
            "1987": "Lionel Messi and Kendrick Lamar",
            "1988": "Stephen Curry and Kevin Durant",
            "1989": "Taylor Swift and Daniel Radcliffe",
            "1990": "Emma Watson and Jennifer Lawrence",
            "1991": "Ed Sheeran and Emma Roberts",
            "1992": "Miley Cyrus and Shawn Johnson",
            "1993": "Ariana Grande and Zayn Malik",
            "1994": "",
            "1995": "",
            "1996": "",
            "1997": "",
            "1998": "",
            "1999": "",
            "2000": "",
            "2001": "",
            "2002": "",
            "2003": "",
            "2004": "",
            "2005": "",
            "2006": "",
            "2007": "",
            "2008": "",
            "2009": "",
            "2010": ""
        };

        // If not empty, mention people
        if (client_birthdate[2] in famous_birthdates && famous_birthdates[client_birthdate[2]] != "") {
            Materialize.toast(famous_birthdates[client_birthdate[2]] + " were also born that year!", 3000)
        }

        // If empty, mention generic comment
        if (client_birthdate[2] in famous_birthdates && famous_birthdates[client_birthdate[2]] == "") {
            Materialize.toast("Oh, " + client_birthdate[2] + " was a fantastic year!")
        }
    }

}