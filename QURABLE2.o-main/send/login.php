<?php
    $firstname = $_POST['fullname'];
    $Email = $_POST['email'];
    $pass = $_POST['password'];
    $cpass = $_POST['confirm_password'];

    //create database

    $conn = new mysqli('localhost','root','','qurable');
    if($conn->connect_error){
        die('Connection Failed : '.$conn->connect_error);
    }
    else{
        $stmt = $conn->prepare("insert into registration(fname,lname,email,dd,uname,pword,phone) 
            value(?,?,?,?,?,?,?)");
        $stmt->bind_param("ssssssi",$firstname,$Email,$pass,$cpass);
        $stmt->execute();
        echo "You Logged In..";
        $stmt->close();
        $conn->close();

    }
    
?>