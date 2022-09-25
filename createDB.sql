# Create TABLE 'Customer'
CREATE TABLE `Customer` (
  `username` varchar(50) NOT NULL,

  `last_name` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `last_login_time` time NOT NULL,
  `last_login_date` date NOT NULL,
  

  PRIMARY KEY(username)
);


# Create TABLE 'ADMIN'
CREATE TABLE `Admin` (
  `username` varchar(50) NOT NULL,

  `last_name` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `last_login_time` time NOT NULL,
  `last_login_date` date NOT NULL,

  PRIMARY KEY(username)
);


# Create TABLE 'ACCOUNT'
CREATE TABLE `Account` (
  `account_id` int NOT NULL,
  `username` varchar(50) NOT NULL,

  `account_number` int NOT NULL,
  `balance` int NOT NULL,
  `currency` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,

  PRIMARY KEY(account_id),
  FOREIGN KEY(username) REFERENCES Customer(username)
);



# Create TABLE 'TRANSACTION'
CREATE TABLE `Transaction` (
  `transaction_id` int NOT NULL,
  `receiver_id` int NOT NULL,
  `sender_id` int NOT NULL,

  `date` date NOT NULL,
  `time` time NOT NULL,
  `amount` int NOT NULL,

  PRIMARY KEY(transaction_id),
  FOREIGN KEY(receiver_id) REFERENCES Account(account_id),
  FOREIGN KEY(sender_id) REFERENCES Account(account_id)
);


# Create TABLE 'CUSTOMER_LOGIN_HISTORY'
CREATE TABLE `Customer_Login_History` (
  `login_id` int NOT NULL,
  `username` varchar(50) NOT NULL,

  `login_date` date NOT NULL,
  `login_time` time NOT NULL,


  PRIMARY KEY(login_id),
  FOREIGN KEY(username) REFERENCES Customer(username)
);

# Create TABLE 'Admin_LOGIN_HISTORY'
CREATE TABLE `Admin_Login_History` (
  `login_id` int NOT NULL,
  `username` varchar(50) NOT NULL,

  `login_date` date NOT NULL,
  `login_time` time NOT NULL,

  PRIMARY KEY(login_id),
  FOREIGN KEY(username) REFERENCES Admin(username)
);
