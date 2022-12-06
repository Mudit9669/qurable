<?php
    $firstname = $_POST['fname'];
    $lastname = $_POST['lname'];
    $Email = $_POST['email'];
    $bday = $_POST['dd'];
    $luser = $_POST['uname'];
    $lpass = $_POST['pword'];
    $pnum = $_POST['phone'];

    //create database

    $conn = new mysqli('localhost','root','','qurable');
    if($conn->connect_error){
        die('Connection Failed : '.$conn->connect_error);
    }
    else{
        $stmt = $conn->prepare("insert into registration(fname,lname,email,dd,uname,pword,phone) 
            value(?,?,?,?,?,?,?)");
        $stmt->bind_param("ssssssi",$firstname,$lastname,$Email,$bday,$luser,$lpass,$pnum);
        $stmt->execute();
        echo "appoinment is booked...";
        $stmt->close();
        $conn->close();

    }
    
?>