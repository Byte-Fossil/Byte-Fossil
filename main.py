import random

print("Hello to a program that will help you answer diifenrent quizs \n.")

#Computer fundamentals
que1 = [
    "The brain of the computer is called", "The CPU", "The RAM", "The GPU",
    "The PSU", 1
]
que2 = [
    "The most common type of software is :", "System software",
    "Application software", "Utility software", "Driver software", 2
]
que3 = ["The basic unit of data is :", "Bit", "Byte", "Word", "Nibble", 1]
que4 = [
    "An interpreter : ",
    "Converts high-level language into machine language line by line",
    "Converts high-level language into machine language before execution",
    "Executes machine code directly ", "NOTA", 1
]
que5 = [
    "A virus is a type of :", "Hardware component", "SOftware component",
    "Network device", "Nota", 2
]
que6 = [
    "Which of the following is not a type of OS", "Batch", "Distributed",
    "Real-time", "Analog", 4
]
que7 = [
    "The binary code used torepresent characters is called :", "ASCII",
    "Unicode", "EBCDIC", "All of the avobe", 4
]
que8 = [
    "The process of breaking down data into packet for ttransmission over a network is called",
    "Encapsulation", "Segmentation", "Packetization", "MMultiplex", 3
]
que9 = [
    "What is the purpose of a debugger ?", "To write code",
    "To find and fix errors in code ", "To compile code", "To execute code", 2
]
que10 = [
    "Cache memory is used for :", "Stores data permanently",
    "Improves CPU performance by storing frequently used data",
    "Stores data temporarily", "Nota", 2
]

#HTML

que11 = [
    " HTML stands for: ", "Hyper Text Markup Language",
    "Hyper Transfer Markup Language", "Hyper Text Machine Language",
    "High Text Markup Language", 1
]
que12 = [
    "What is the correct syntax for an HTML tag?", "<tag>content</tag>",
    "{tag}content{/tag}", "[tag]content[/tag]", "#tag#content#tag#", 1
]
que13 = [
    "The root element of an HTML page is:", "<head>", "<body>", "<html>",
    "<div>", 3
]
que14 = [
    "Which tag is used to define a hyperlink?", "<link>", "<a>", "<ref>",
    "<url>", 2
]
que15 = [
    "The tag used to define a table row is:", "<table>", "<tr>", "<td>",
    "<th>", 2
]
que16 = [
    "Which tag is used to group table header content in a single line?",
    "<thead>", "<tbody>", "<tfoot>", "<colgroup>", 1
]
que17 = [
    "The input type used for a drop-down list is:", "text", "password",
    "submit", "select", 4
]
que18 = [
    "The tag used to embed another HTML document within a current HTML document is:",
    "<frameset>", "<frame>", "<iframe>", "<div>", 3
]
que19 = [
    "The <article> element is used for:", "Defining navigation links",
    "Defining content", "Defining independent, self-contained content",
    "Defining page footer", 3
]
que20 = [
    "The attribute used to merge table cells vertically is:", "colspan",
    "rowspan", "merge", "combine", 2
]

#Opering System
que21 = [
    "The most common type of operating system is:", "Batch", "Distributed",
    "Multi-user", "Real-time", 3
]
que22 = [
    "The core part of an operating system is:", "Kernel", "Shell",
    "Application", "Device driver", 1
]
que23 = [
    "What is the process of loading the operating system into computer memory called?",
    "Booting", "Caching", "Paging", "Swapping", 1
]
que24 = [
    "The user interface of an operating system is:",
    "The way a user interacts with the computer", "The hardware components",
    "The software applications", "The internal processes", 1
]
que25 = [
    "A GUI stands for:", "Graphical User Interface",
    "Graphic User Interaction", "General User Interface",
    "Global User Interface", 1
]
que26 = [
    "The process of transferring files from a computer to a remote server is called:",
    "Uploading", "Downloading", "Copying", "Pasting", 1
]
que27 = [
    "What is the purpose of a file system?",
    "To organize and manage files on a storage device", "To run applications",
    "To control hardware devices", "To provide user interface", 1
]
que28 = [
    "The internet is a vast network of:", "Computers", "Servers", "Networks",
    "All of the above", 4
]
que29 = [
    "Which protocol is used for sending emails?", "HTTP", "FTP", "SMTP", "TCP",
    3
]
que30 = [
    "A firewall is used to:",
    "Protect a computer network from unauthorized access",
    "Speed up internet connection", "Remove viruses", "Store data", 1
]

#Computer Networking
que31 = [
    "A network is defined as:", "A collection of hardware components",
    "A group of interconnected computers", "A software application",
    "A storage device", 2
]
que32 = [
    "The topology in which all computers are connected to a central hub is called:",
    "Star topology", "Bus topology", "Ring topology", "Mesh topology", 1
]
que33 = [
    "The device used to connect multiple networks is called:", "Hub", "Switch",
    "Router", "Modem", 3
]
que34 = [
    "The protocol used to transfer data over the internet is:", "HTTP", "FTP",
    "TCP/IP", "SMTP", 3
]
que35 = [
    "A network that spans a large geographical area is called:", "LAN", "MAN",
    "WAN", "PAN", 3
]
que36 = [
    "The speed at which data can be transmitted over a network is called:",
    "Bandwidth", "Latency", "Th=roughput", "Capacity", 1
]
que37 = [
    "The address of a computer on a network is called:", "IP address",
    "MAC address", "URL", "DNS", 1
]
que38 = [
    "Which of the following is a wireless network technology?", "Wi-Fi",
    "Ethernet", "Bluetooth", "All of the above", 4
]
que39 = [
    "The process of converting digital signals into analog signals is called:",
    "Modulation", "Demodulation", "Digitization", "Analogization", 2
]
que40 = [
    "The process of converting analog signals into digital signals is called:",
    "Modulation", "Demodulation", "Digitization", "Analogization", 3
]

#Ms office 2009

que41 = [
    "MS Word is primarily used for:", "Creating spreadsheets",
    "Developing presentations", "Creating and editing text documents",
    "Database management", 3
]
que42 = [
    "Which feature in MS Word is used to check spelling and grammar?",
    "Spell Check", "Grammar Check", "AutoCorrect", "All of the above", 4
]
que43 = [
    "The alignment options in MS Word are:", "Left, Right, Center, Justify",
    "Top, Bottom, Center", "Normal, Heading 1, Heading 2", "None of the above",
    1
]
que44 = [
    "MS Excel is primarily used for:", "Creating presentations",
    "Image editing", "Data analysis and calculations", "Web development", 3
]
que45 = [
    "MS PowerPoint is primarily used for:", "Creating documents",
    "Database management", "Creating presentations", "Data analysis", 3
]
que46 = [
    "The basic building blocks of a PowerPoint presentation are called:",
    "Slides", "Layouts", "Designs", "Themes", 1
]
que47 = [
    "MS Access is primarily used for:", "Creating documents",
    "Creating presentations", "Database management", "Image editing", 3
]
que48 = [
    "The primary key in a table is:", "A unique identifier for each record",
    "A field that can contain duplicate values",
    "A field that is not required", "A calculated field", 1
]
que49 = [
    "The header and footer sections in MS Word are located:",
    "At the top and bottom of every page",
    "At the beginning and end of the document", "In the margins",
    "None of the above", 1
]
que50 = [
    "A pivot table in MS Excel is used to:", "Summarize and analyze data",
    "Create charts", "Format data", "Calculate formulas", 1
]

#Ms Access

que51 = [
    "MS Access is a:", "Word Processor", "Database Management System",
    "Spreadsheet", "Presentation Software", 2
]
que52 = [
    "The basic building blocks of a database are:", "Tables", "Queries",
    "Forms", "Reports", 1
]
que53 = [
    "A query is used to:", "Retrieve specific data from a table",
    "Modify data in a table", "Create a new table", "Print a report", 1
]
que54 = [
    "A report is used to:", "Present data in a printed format",
    "Enter data into a table", "Create a query", "Design a form", 1
]
que55 = [
    "A filter is used to:", "Display specific records based on criteria",
    "Sort records in a table", "Create a new table", "Modify data", 1
]
que56 = [
    "A form can be used to:", "Enter data", "Edit data", "Display data",
    "All of the above", 4
]
que57 = [
    "A report can be used to:", "Print data in a formatted layout",
    "Create a new table", "Modify existing data", "Enter data", 1
]
que58 = [
    "A macro is used to:", "Automate tasks", "Create a form",
    "Design a report", "Modify data", 1
]
que59 = [
    "A relational database is a database that:",
    "Stores data in related tables", "Stores data in a single table",
    "Stores data in a hierarchical structure",
    "Stores data in a network structure", 1
]
que60 = [
    "The process of ensuring data accuracy and consistency is called:",
    "Data validation", "Data entry", "Data analysis", "Data mining", 1
]

#World Wide Web

que61 = [
    "The World Wide Web is a part of:", "Internet", "LAN", "WAN", "MAN", 1
]
que62 = [
    "The inventor of the World Wide Web is:", "Bill Gates", "Steve Jobs",
    "Tim Berners-Lee", "Mark Zuckerberg", 3
]
que63 = [
    "The protocol used to transfer web pages is:", "HTTP", "FTP", "SMTP",
    "POP3", 1
]
que64 = [
    "A unique address of a resource on the internet is called:", "URL",
    "IP address", "Domain name", "Host name", 1
]
que65 = [
    "A hyperlink is used to:", "Link to another web page",
    "Create a new web page", "Display an image", "All of the above", 1
]
que66 = [
    "Social media is a platform for:", "Connecting with people",
    "Sharing information", "Building relationships", "All of the above", 4
]
que67 = [
    "The most popular social media platform is:", "Facebook", "Twitter",
    "Instagram", "Reddit", 1
]
que68 = [
    "Cybercrime refers to:", "Crimes committed using computers",
    "Crimes against computers", "Crimes related to computers",
    "All of the above", 4
]
que69 = [
    "Online privacy is important because:", "It protects personal information",
    "It prevents identity theft", "It ensures secure online transactions",
    "All of the above", 4
]
que70 = [
    "Plagiarism is:", "Using someone else's work without giving credit",
    "Copying software", "Hacking a computer", "All of the above", 1
]
que70_2 = [
    "Netiquette refers to:", "Internet etiquette", "Network etiquette",
    "Computer etiquette", "All of the above", 1
]

#Communication Technology

que71 = [
    "The basic elements of communication are:",
    "Sender, receiver, message, channel, noise",
    "Sender, receiver, message, channel", "Sender, receiver, message",
    "Sender, receiver", 1
]
que72 = [
    "The internet is a global network of:", "Computers", "Phones",
    "Televisions", "Radios", 1
]
que73 = [
    "To protect yourself online, you should avoid:",
    "Sharing personal information", "Using strong passwords",
    "Being cautious of phishing attempts", "Updating your software", 1
]
que74 = [
    "The process of converting data into a code to hide its meaning is called:",
    "Encryption", "Decryption", "Steganography", "Cryptography", 1
]
que75 = [
    "The concept of using multiple servers to distribute workload is known as:",
    "Load balancing", "Clustering", "Virtualization", "Cloud computing", 1
]
que76 = [
    "The ability to access and manipulate data from any location with an internet connection is called:",
    "Cloud computing", "Big data", "Internet of Things",
    "Artificial intelligence", 1
]
que77 = [
    "A DNS server translates domain names into:", "IP addresses",
    "MAC addresses", "Physical addresses", "Port numbers", 1
]
que78 = [
    "The speed of data transmission is measured in:", "Bits per second (bps)",
    "Bytes per second (Bps)", "Kilobytes per second (Kbps)",
    "All of the above", 4
]
que79 = [
    "A VPN is used to create a secure connection over an insecure network:",
    "True", "False", "", "", 1
]
que80 = [
    "Which multiplexing technique is commonly used in cable television?",
    "Frequency Division Multiplexing (FDM)",
    "Time Division Multiplexing (TDM)", "Code Division Multiple Access (CDMA)",
    "Wavelength Division Multiplexing (WDM)", 1
]

#Declarations

computer_fundamentals_que = [
    que1, que2, que3, que4, que5, que6, que7, que8, que9, que10
]
computer_fundamentals = []

html_que = [
    que11, que12, que13, que14, que15, que16, que17, que18, que19, que20
]
html = []

operating_system_que = [
    que21, que22, que23, que24, que25, que26, que27, que28, que29, que30
]
operating_system = []

computer_networking_que = [
    que31, que32, que33, que34, que35, que36, que37, que38, que39, que40
]
computer_networking = []

ms_office_que = [
    que41, que42, que43, que44, que45, que46, que47, que48, que49, que50
]
ms_office_2009 = []

ms_access_que = [
    que51, que52, que53, que54, que55, que56, que57, que58, que59, que60
]
ms_access = []

world_wide_web_que = [
    que61, que62, que63, que64, que65, que66, que67, que68, que69, que70
]
world_wide_web = []

communication_technology_que = [
    que71, que72, que73, que74, que75, que76, que77, que78, que79, que80
]
communication_technology = []

correct_answers = 0

#Functions


def check_answer(computer_fundamentals_que, computer_fundamentals, name):
    global correct_answers
    print(
        f"These are the questions of the topic  {name}\n-----:-----------------------------------------------:------"
    )
    # Making a shuffled lists of questions
    ques = computer_fundamentals_que
    random.shuffle(ques)
    for j in range(0, 5):
        ques.pop(random.randint(0, 9 - j))
    # Printing the questions
    for i in range(0, 5):
        question = ques[i]
        print(
            f"{question[0]}\n\n a) {question[1]}\n b) {question[2]}\n c) {question[3]}\n d) {question[4]}"
        )
        answer = int(input("\nEnter your answer (1-4): "))
        if answer == question[5]:
            print("Correct answer!\n")
            correct_answers += 1
        else:
            print(f"Wrong answer! The correct answer is {question[5]} \n")


#Execution

check_answer(computer_fundamentals_que, computer_fundamentals,
             "Computer Fundamentals")
check_answer(html_que, html, "HTML")
check_answer(operating_system_que, operating_system, "Operating System")
check_answer(computer_networking_que, computer_networking,
             "Computer Networking")
check_answer(ms_office_que, ms_office_2009, "MS Office")
check_answer(ms_access_que, ms_access, "MS Access")
check_answer(world_wide_web_que, world_wide_web, "World Wide Web")
check_answer(communication_technology_que, communication_technology,
             "Communication Technology")

print(f"You got {correct_answers} out of 40 correct answers.")
