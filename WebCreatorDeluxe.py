"""
Version: .1
Author: Dylan Smith
Date: August 2, 2022
"""

from ctypes import alignment
from functools import total_ordering
import tkinter as tk

root = tk.Tk()
root.geometry("800x350")
root.title("Website Builder Deluxe v.3")


totalCount = 0
countAllAutos = 0
countCars = 0
countTrucks = 0
countSUVs = 0
countVans = 0
countAllCampers = 0
countRush = 0
countShasta = 0
countForestRiver = 0

#########################################################INITIALIZE ALL OF THE FILES
def CreateFiles():
    index = open("index.html", "w")
    index.write("""
<!DOCTYPE html>
<html lang="en">
<body id="wrapper">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="rhonda.css">
        <title>Rhonda's RV/Auto</title>
        <link rel="icon" type="image/x-icon" href="http://rhondasrvandauto.com/photo/RhondaIcon.ico">
        <meta name="description" content="Rhonda's RV and Auto is a buy here pay here car lot. All of our vehicles are sold AS-IS with no warranty. Check out everything we have to sale right at this moment on our official website">
        <meta name="keywords" content="Used Cars, Campers, Rhonda's Rv and Auto, Rhonda's, Car Lot">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
<header id="rcorners1">
Rhonda's RV & Auto
</header>
<nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/index.html">Home</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/index.html">Home</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/camper/AllCampers.html">Campers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/camper/ForestRiver.html">Forest River</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Shasta.html">Shasta</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Rush.html">Rush</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/AllCampers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/auto/AllAuto.html">Auto</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/auto/Cars.html">Cars</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Trucks.html">Trucks</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/SUVs.html">SUVs</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Vans.html">Vans</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/AllAuto.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">Trailers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/trailer/Enclosed.html">Enclosed Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/CarTrailers.html">Car Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/Information.html">Information</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/Information.html">Location</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Phone</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Email</a></p>
    </div>
</nav>
</nav>
<div id="headImage">
    <img src="http://rhondasrvandauto.com/photo/RhondaImage.png" alt="Picture of Rhonda's RV and Auto.">
</div>
<div id="listbg">
    <h1>Welcome to Rhonda's RV and Auto! <br>Our Recent Vehicles</h1>
    """)
    index.close()

    allAuto = open("AllAuto.html", "w")
    allAuto.write("""
<!DOCTYPE html>
<html lang="en">
<body id="wrapper">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="rhonda.css">
        <title>Rhonda's RV/Auto</title>
        <link rel="icon" type="image/x-icon" href="http://rhondasrvandauto.com/photo/RhondaIcon.ico">
        <meta name="description" content="Rhonda's RV and Auto is a buy here pay here car lot. All of our vehicles are sold AS-IS with no warranty. Check out everything we have to sale right at this moment on our official website">
        <meta name="keywords" content="Used Cars, Campers, Rhonda's Rv and Auto, Rhonda's, Car Lot">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
<header id="rcorners1">
Rhonda's RV & Auto
</header>
<nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/index.html">Home</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/index.html">Home</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/camper/AllCampers.html">Campers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/camper/ForestRiver.html">Forest River</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Shasta.html">Shasta</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Rush.html">Rush</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/AllCampers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/auto/AllAuto.html">Auto</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/auto/Cars.html">Cars</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Trucks.html">Trucks</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/SUVs.html">SUVs</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Vans.html">Vans</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/AllAuto.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">Trailers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/trailer/Enclosed.html">Enclosed Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/CarTrailers.html">Car Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/Information.html">Information</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/Information.html">Location</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Phone</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Email</a></p>
    </div>
</nav>
</nav>
<div id="headImage">
    <img src="http://rhondasrvandauto.com/photo/RhondaImage.png" alt="Picture of Rhonda's RV and Auto.">
</div>
<div id="listbg">
    <h1>All of our Vehicles Currently</h1>
    """)
    allAuto.close()

    cars = open("Cars.html", "w")
    cars.write("""
<!DOCTYPE html>
<html lang="en">
<body id="wrapper">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="rhonda.css">
        <title>Rhonda's RV/Auto</title>
        <link rel="icon" type="image/x-icon" href="http://rhondasrvandauto.com/photo/RhondaIcon.ico">
        <meta name="description" content="Rhonda's RV and Auto is a buy here pay here car lot. All of our vehicles are sold AS-IS with no warranty. Check out everything we have to sale right at this moment on our official website">
        <meta name="keywords" content="Used Cars, Campers, Rhonda's Rv and Auto, Rhonda's, Car Lot">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
<header id="rcorners1">
Rhonda's RV & Auto
</header>
<nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/index.html">Home</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/index.html">Home</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/camper/AllCampers.html">Campers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/camper/ForestRiver.html">Forest River</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Shasta.html">Shasta</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Rush.html">Rush</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/AllCampers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/auto/AllAuto.html">Auto</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/auto/Cars.html">Cars</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Trucks.html">Trucks</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/SUVs.html">SUVs</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Vans.html">Vans</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/AllAuto.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">Trailers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/trailer/Enclosed.html">Enclosed Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/CarTrailers.html">Car Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/Information.html">Information</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/Information.html">Location</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Phone</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Email</a></p>
    </div>
</nav>
</nav>
<div id="headImage">
    <img src="http://rhondasrvandauto.com/photo/RhondaImage.png" alt="Picture of Rhonda's RV and Auto.">
</div>
<div id="listbg">
    <h1>Our Cars on the Lot</h1>
    """)
    cars.close()    

    trucks = open("Trucks.html", "w")
    trucks.write("""
<!DOCTYPE html>
<html lang="en">
<body id="wrapper">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="rhonda.css">
        <title>Rhonda's RV/Auto</title>
        <link rel="icon" type="image/x-icon" href="http://rhondasrvandauto.com/photo/RhondaIcon.ico">
        <meta name="description" content="Rhonda's RV and Auto is a buy here pay here car lot. All of our vehicles are sold AS-IS with no warranty. Check out everything we have to sale right at this moment on our official website">
        <meta name="keywords" content="Used Cars, Campers, Rhonda's Rv and Auto, Rhonda's, Car Lot">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
<header id="rcorners1">
Rhonda's RV & Auto
</header>
<nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/index.html">Home</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/index.html">Home</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/camper/AllCampers.html">Campers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/camper/ForestRiver.html">Forest River</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Shasta.html">Shasta</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Rush.html">Rush</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/AllCampers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/auto/AllAuto.html">Auto</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/auto/Cars.html">Cars</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Trucks.html">Trucks</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/SUVs.html">SUVs</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Vans.html">Vans</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/AllAuto.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">Trailers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/trailer/Enclosed.html">Enclosed Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/CarTrailers.html">Car Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/Information.html">Information</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/Information.html">Location</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Phone</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Email</a></p>
    </div>
</nav>
</nav>
<div id="headImage">
    <img src="http://rhondasrvandauto.com/photo/RhondaImage.png" alt="Picture of Rhonda's RV and Auto.">
</div>
<div id="listbg">
    <h1>Our Trucks on the Lot</h1>
    """)
    trucks.close()

    SUVs = open("SUVs.html", "w")
    SUVs.write("""
<!DOCTYPE html>
<html lang="en">
<body id="wrapper">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="rhonda.css">
        <title>Rhonda's RV/Auto</title>
        <link rel="icon" type="image/x-icon" href="http://rhondasrvandauto.com/photo/RhondaIcon.ico">
        <meta name="description" content="Rhonda's RV and Auto is a buy here pay here car lot. All of our vehicles are sold AS-IS with no warranty. Check out everything we have to sale right at this moment on our official website">
        <meta name="keywords" content="Used Cars, Campers, Rhonda's Rv and Auto, Rhonda's, Car Lot">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
<header id="rcorners1">
Rhonda's RV & Auto
</header>
<nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/index.html">Home</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/index.html">Home</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/camper/AllCampers.html">Campers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/camper/ForestRiver.html">Forest River</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Shasta.html">Shasta</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Rush.html">Rush</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/AllCampers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/auto/AllAuto.html">Auto</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/auto/Cars.html">Cars</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Trucks.html">Trucks</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/SUVs.html">SUVs</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Vans.html">Vans</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/AllAuto.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">Trailers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/trailer/Enclosed.html">Enclosed Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/CarTrailers.html">Car Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/Information.html">Information</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/Information.html">Location</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Phone</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Email</a></p>
    </div>
</nav>
</nav>
<div id="headImage">
    <img src="http://rhondasrvandauto.com/photo/RhondaImage.png" alt="Picture of Rhonda's RV and Auto.">
</div>
<div id="listbg">
    <h1>Our SUVs on the Lot</h1>
    """)
    SUVs.close()

    vans = open("Vans.html", "w")
    vans.write("""
<!DOCTYPE html>
<html lang="en">
<body id="wrapper">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="rhonda.css">
        <title>Rhonda's RV/Auto</title>
        <link rel="icon" type="image/x-icon" href="http://rhondasrvandauto.com/photo/RhondaIcon.ico">
        <meta name="description" content="Rhonda's RV and Auto is a buy here pay here car lot. All of our vehicles are sold AS-IS with no warranty. Check out everything we have to sale right at this moment on our official website">
        <meta name="keywords" content="Used Cars, Campers, Rhonda's Rv and Auto, Rhonda's, Car Lot">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
<header id="rcorners1">
Rhonda's RV & Auto
</header>
<nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/index.html">Home</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/index.html">Home</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/camper/AllCampers.html">Campers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/camper/ForestRiver.html">Forest River</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Shasta.html">Shasta</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Rush.html">Rush</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/AllCampers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/auto/AllAuto.html">Auto</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/auto/Cars.html">Cars</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Trucks.html">Trucks</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/SUVs.html">SUVs</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Vans.html">Vans</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/AllAuto.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">Trailers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/trailer/Enclosed.html">Enclosed Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/CarTrailers.html">Car Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/Information.html">Information</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/Information.html">Location</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Phone</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Email</a></p>
    </div>
</nav>
</nav>
<div id="headImage">
    <img src="http://rhondasrvandauto.com/photo/RhondaImage.png" alt="Picture of Rhonda's RV and Auto.">
</div>
<div id="listbg">
    <h1>Our Vans on the Lot</h1>
    """)
    vans.close()

    allCampers = open("AllCampers.html", "w")
    allCampers.write("""
<!DOCTYPE html>
<html lang="en">
<body id="wrapper">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="rhonda.css">
        <title>Rhonda's RV/Auto</title>
        <link rel="icon" type="image/x-icon" href="http://rhondasrvandauto.com/photo/RhondaIcon.ico">
        <meta name="description" content="Rhonda's RV and Auto is a buy here pay here car lot. All of our vehicles are sold AS-IS with no warranty. Check out everything we have to sale right at this moment on our official website">
        <meta name="keywords" content="Used Cars, Campers, Rhonda's Rv and Auto, Rhonda's, Car Lot">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
<header id="rcorners1">
Rhonda's RV & Auto
</header>
<nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/index.html">Home</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/index.html">Home</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/camper/AllCampers.html">Campers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/camper/ForestRiver.html">Forest River</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Shasta.html">Shasta</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Rush.html">Rush</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/AllCampers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/auto/AllAuto.html">Auto</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/auto/Cars.html">Cars</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Trucks.html">Trucks</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/SUVs.html">SUVs</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Vans.html">Vans</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/AllAuto.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">Trailers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/trailer/Enclosed.html">Enclosed Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/CarTrailers.html">Car Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/Information.html">Information</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/Information.html">Location</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Phone</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Email</a></p>
    </div>
</nav>
</nav>
<div id="headImage">
    <img src="http://rhondasrvandauto.com/photo/RhondaImage.png" alt="Picture of Rhonda's RV and Auto.">
</div>
<div id="listbg">
    <h1>Our Campers on the Lot</h1>
    """)
    allCampers.close()

    forestRiver = open("ForestRiver.html", "w")
    forestRiver.write("""
<!DOCTYPE html>
<html lang="en">
<body id="wrapper">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="rhonda.css">
        <title>Rhonda's RV/Auto</title>
        <link rel="icon" type="image/x-icon" href="http://rhondasrvandauto.com/photo/RhondaIcon.ico">
        <meta name="description" content="Rhonda's RV and Auto is a buy here pay here car lot. All of our vehicles are sold AS-IS with no warranty. Check out everything we have to sale right at this moment on our official website">
        <meta name="keywords" content="Used Cars, Campers, Rhonda's Rv and Auto, Rhonda's, Car Lot">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
<header id="rcorners1">
Rhonda's RV & Auto
</header>
<nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/index.html">Home</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/index.html">Home</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/camper/AllCampers.html">Campers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/camper/ForestRiver.html">Forest River</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Shasta.html">Shasta</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Rush.html">Rush</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/AllCampers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/auto/AllAuto.html">Auto</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/auto/Cars.html">Cars</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Trucks.html">Trucks</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/SUVs.html">SUVs</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Vans.html">Vans</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/AllAuto.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">Trailers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/trailer/Enclosed.html">Enclosed Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/CarTrailers.html">Car Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/Information.html">Information</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/Information.html">Location</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Phone</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Email</a></p>
    </div>
</nav>
</nav>
<div id="headImage">
    <img src="http://rhondasrvandauto.com/photo/RhondaImage.png" alt="Picture of Rhonda's RV and Auto.">
</div>
<div id="listbg">
    <h1>Forest River Campers</h1>
    """)
    forestRiver.close()

    rush = open("Rush.html", "w")
    rush.write("""
<!DOCTYPE html>
<html lang="en">
<body id="wrapper">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="rhonda.css">
        <title>Rhonda's RV/Auto</title>
        <link rel="icon" type="image/x-icon" href="http://rhondasrvandauto.com/photo/RhondaIcon.ico">
        <meta name="description" content="Rhonda's RV and Auto is a buy here pay here car lot. All of our vehicles are sold AS-IS with no warranty. Check out everything we have to sale right at this moment on our official website">
        <meta name="keywords" content="Used Cars, Campers, Rhonda's Rv and Auto, Rhonda's, Car Lot">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
<header id="rcorners1">
Rhonda's RV & Auto
</header>
<nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/index.html">Home</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/index.html">Home</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/camper/AllCampers.html">Campers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/camper/ForestRiver.html">Forest River</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Shasta.html">Shasta</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Rush.html">Rush</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/AllCampers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/auto/AllAuto.html">Auto</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/auto/Cars.html">Cars</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Trucks.html">Trucks</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/SUVs.html">SUVs</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Vans.html">Vans</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/AllAuto.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">Trailers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/trailer/Enclosed.html">Enclosed Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/CarTrailers.html">Car Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/Information.html">Information</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/Information.html">Location</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Phone</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Email</a></p>
    </div>
</nav>
</nav>
<div id="headImage">
    <img src="http://rhondasrvandauto.com/photo/RhondaImage.png" alt="Picture of Rhonda's RV and Auto.">
</div>
<div id="listbg">
    <h1>Rush Campers</h1>
    """)
    rush.close()

    shasta = open("Shasta.html", "w")
    shasta.write("""
<!DOCTYPE html>
<html lang="en">
<body id="wrapper">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="rhonda.css">
        <title>Rhonda's RV/Auto</title>
        <link rel="icon" type="image/x-icon" href="http://rhondasrvandauto.com/photo/RhondaIcon.ico">
        <meta name="description" content="Rhonda's RV and Auto is a buy here pay here car lot. All of our vehicles are sold AS-IS with no warranty. Check out everything we have to sale right at this moment on our official website">
        <meta name="keywords" content="Used Cars, Campers, Rhonda's Rv and Auto, Rhonda's, Car Lot">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
<header id="rcorners1">
Rhonda's RV & Auto
</header>
<nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/index.html">Home</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/index.html">Home</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/camper/AllCampers.html">Campers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/camper/ForestRiver.html">Forest River</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Shasta.html">Shasta</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/Rush.html">Rush</a></p>
    <p><a href="http://rhondasrvandauto.com/camper/AllCampers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/auto/AllAuto.html">Auto</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/auto/Cars.html">Cars</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Trucks.html">Trucks</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/SUVs.html">SUVs</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/Vans.html">Vans</a></p>
    <p><a href="http://rhondasrvandauto.com/auto/AllAuto.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">Trailers</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/trailer/Enclosed.html">Enclosed Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/CarTrailers.html">Car Trailers</a></p>
    <p><a href="http://rhondasrvandauto.com/trailer/AllTrailers.html">All</a></p>
    </div>
</nav>
<nav class="dropdown">
    <span><a href="http://rhondasrvandauto.com/Information.html">Information</a></span>
    <div class="dropdown-content">
    <p><a href="http://rhondasrvandauto.com/Information.html">Location</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Phone</a></p>
    <p><a href="http://rhondasrvandauto.com/Information.html">Email</a></p>
    </div>
</nav>
</nav>
<div id="headImage">
    <img src="http://rhondasrvandauto.com/photo/RhondaImage.png" alt="Picture of Rhonda's RV and Auto.">
</div>
<div id="listbg">
    <h1>Shasta Campers</h1>
    """)
    shasta.close()

def FinishFiles():
    index = open("index.html", "a")

    allAuto = open("AllAuto.html", "a")

    cars = open("Cars.html", "a")

    trucks = open("Trucks.html", "a")

    SUVs = open("SUVs.html", "a")

    vans = open("Vans.html", "a")

    allCampers = open("AllCampers.html", "a")

    forestRiver = open("ForestRiver.html", "a")

    rush = open("Rush.html", "a")

    shasta = open("Shasta.html", "a")

def AddtoSite():
    global totalCount, countAllAutos, countCars, countTrucks, countSUVs, countVans, countAllCampers, countRush, countForestRiver, countShasta
    imageName = makeModel.get().replace(" ", "")+"_"+VIN.get()
    print(imageName)
    # if checkbutton is active, checkbutton = 1
    #loop for divs
    #access the associated checkbuttons file and append html

    if varAllAutos.get() == 1:
        allAuto = open("AllAuto.html", "a")
        
        if countAllAutos == 0:
            allAuto.write("""   <div id="list">""")
        
        allAuto.write(f"""
    <div id="#rcorners3" class="panel">
        <h1 class="panel__header">{year.get()} {makeModel.get()}</h1>

        <div class="SlideHolder">
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_1.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_2.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_3.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_4.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_5.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
            <a id="LeftButton" onclick="plusSlides(-1, {totalCount})">&#10094</a>
            <a id="RightButton" onclick="plusSlides(1, {totalCount})">&#10095</a>
        </div>
        
        <table class="panel__body">
            <tr>
            <td class="panel_bold">Year</td>
            <td>{year.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Miles</td>
            <td>{miles.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Engine</td>
            <td>{engine.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Exterior Color</td>
            <td>{extColor.get()}</td>
            </tr>
        </table>
      </div>
        """)
        if countAllAutos == 2:
            allAuto.write("""  </div>""")
            countAllAutos = 0
        else:
            countAllAutos = countAllAutos + 1
        allAuto.close()

    if varCars.get() == 1:
        cars = open("Cars.html", "a")
        if countCars == 0:
            cars.write("""   <div id="list">""")
        
        cars.write(f"""
    <div id="#rcorners3" class="panel">
        <h1 class="panel__header">{year.get()} {makeModel.get()}</h1>

        <div class="SlideHolder">
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_1.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_2.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_3.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_4.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_5.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
            <a id="LeftButton" onclick="plusSlides(-1, {totalCount})">&#10094</a>
            <a id="RightButton" onclick="plusSlides(1, {totalCount})">&#10095</a>
        </div>
        
        <table class="panel__body">
            <tr>
            <td class="panel_bold">Year</td>
            <td>{year.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Miles</td>
            <td>{miles.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Engine</td>
            <td>{engine.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Exterior Color</td>
            <td>{extColor.get()}</td>
            </tr>
        </table>
      </div>
        """)
        if countCars == 2:
            cars.write("""  </div>""")
            countCars = 0
        else:
            countCars = countCars + 1
        cars.close()

    if varTrucks.get() == 1:
        trucks = open("Trucks.html", "a")
        if countTrucks == 0:
            trucks.write("""   <div id="list">""")
        
        trucks.write(f"""
    <div id="#rcorners3" class="panel">
        <h1 class="panel__header">{year.get()} {makeModel.get()}</h1>

        <div class="SlideHolder">
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_1.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_2.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_3.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_4.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_5.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
            <a id="LeftButton" onclick="plusSlides(-1, {totalCount})">&#10094</a>
            <a id="RightButton" onclick="plusSlides(1, {totalCount})">&#10095</a>
        </div>
        
        <table class="panel__body">
            <tr>
            <td class="panel_bold">Year</td>
            <td>{year.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Miles</td>
            <td>{miles.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Engine</td>
            <td>{engine.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Exterior Color</td>
            <td>{extColor.get()}</td>
            </tr>
        </table>
      </div>
        """)
        if countTrucks == 2:
            trucks.write("""  </div>""")
            countTrucks = 0
        else:
            countTrucks = countTrucks + 1
        trucks.close()

    if varSUVs.get() == 1:
        SUVs = open("SUVs.html", "a")
        if countSUVs == 0:
            SUVs.write("""   <div id="list">""")
        
        SUVs.write(f"""
    <div id="#rcorners3" class="panel">
        <h1 class="panel__header">{year.get()} {makeModel.get()}</h1>

        <div class="SlideHolder">
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_1.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_2.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_3.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_4.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_5.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
            <a id="LeftButton" onclick="plusSlides(-1, {totalCount})">&#10094</a>
            <a id="RightButton" onclick="plusSlides(1, {totalCount})">&#10095</a>
        </div>
        
        <table class="panel__body">
            <tr>
            <td class="panel_bold">Year</td>
            <td>{year.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Miles</td>
            <td>{miles.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Engine</td>
            <td>{engine.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Exterior Color</td>
            <td>{extColor.get()}</td>
            </tr>
        </table>
      </div>
        """)
        if countSUVs == 2:
            SUVs.write("""  </div>""")
            countSUVs = 0
        else:
            countSUVs = countSUVs + 1
        SUVs.close()

    if varVans.get() == 1:
        vans = open("Vans.html", "a")
        if countVans == 0:
            vans.write("""   <div id="list">""")
        
        vans.write(f"""
    <div id="#rcorners3" class="panel">
        <h1 class="panel__header">{year.get()} {makeModel.get()}</h1>

        <div class="SlideHolder">
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_1.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_2.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_3.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_4.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_5.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
            <a id="LeftButton" onclick="plusSlides(-1, {totalCount})">&#10094</a>
            <a id="RightButton" onclick="plusSlides(1, {totalCount})">&#10095</a>
        </div>
        
        <table class="panel__body">
            <tr>
            <td class="panel_bold">Year</td>
            <td>{year.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Miles</td>
            <td>{miles.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Engine</td>
            <td>{engine.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Exterior Color</td>
            <td>{extColor.get()}</td>
            </tr>
        </table>
      </div>
        """)
        if countVans == 2:
            vans.write("""  </div>""")
            countVans = 0
        else:
            countVans = countVans + 1
        vans.close()

    if varAllCamper.get() == 1:
        allCampers = open("AllCamper.html", "a")
        if countAllCampers == 0:
            allAuto.write("""   <div id="list">""")
        
        allCampers.write(f"""
    <div id="#rcorners3" class="panel">
        <h1 class="panel__header">{year.get()} {makeModel.get()}</h1>

        <div class="SlideHolder">
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_1.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_2.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_3.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_4.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_5.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
            <a id="LeftButton" onclick="plusSlides(-1, {totalCount})">&#10094</a>
            <a id="RightButton" onclick="plusSlides(1, {totalCount})">&#10095</a>
        </div>
        
        <table class="panel__body">
            <tr>
            <td class="panel_bold">Year</td>
            <td>{year.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Miles</td>
            <td>{miles.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Engine</td>
            <td>{engine.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Exterior Color</td>
            <td>{extColor.get()}</td>
            </tr>
        </table>
      </div>
        """)
        if countAllCampers == 2:
            allCampers.write("""  </div>""")
            countAllCampers = 0
        else:
            countAllCampers = countAllCampers + 1
        allCampers.close()

    if varShasta.get() == 1:
        shasta = open("Shasta.html", "a")
        if countShasta == 0:
            shasta.write("""   <div id="list">""")
        
        shasta.write(f"""
    <div id="#rcorners3" class="panel">
        <h1 class="panel__header">{year.get()} {makeModel.get()}</h1>

        <div class="SlideHolder">
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_1.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_2.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_3.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_4.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_5.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
            <a id="LeftButton" onclick="plusSlides(-1, {totalCount})">&#10094</a>
            <a id="RightButton" onclick="plusSlides(1, {totalCount})">&#10095</a>
        </div>
        
        <table class="panel__body">
            <tr>
            <td class="panel_bold">Year</td>
            <td>{year.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Miles</td>
            <td>{miles.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Engine</td>
            <td>{engine.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Exterior Color</td>
            <td>{extColor.get()}</td>
            </tr>
        </table>
      </div>
        """)
        if countShasta == 2:
            shasta.write("""  </div>""")
            countShasta = 0
        else:
            countShasta = countShasta + 1
        shasta.close()

    if varRush.get() == 1:
        rush = open("Rush.html", "a")
        if countRush == 0:
            rush.write("""   <div id="list">""")
        
        rush.write(f"""
    <div id="#rcorners3" class="panel">
        <h1 class="panel__header">{year.get()} {makeModel.get()}</h1>

        <div class="SlideHolder">
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_1.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_2.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_3.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_4.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_5.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
            <a id="LeftButton" onclick="plusSlides(-1, {totalCount})">&#10094</a>
            <a id="RightButton" onclick="plusSlides(1, {totalCount})">&#10095</a>
        </div>
        
        <table class="panel__body">
            <tr>
            <td class="panel_bold">Year</td>
            <td>{year.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Miles</td>
            <td>{miles.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Engine</td>
            <td>{engine.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Exterior Color</td>
            <td>{extColor.get()}</td>
            </tr>
        </table>
      </div>
        """)
        if countRush == 2:
            rush.write("""  </div>""")
            countRush = 0
        else:
            countRush = countRush + 1
        rush.close()

    if varForestRiver.get() == 1:
        forestRiver = open("ForestRiver.html", "a")
        if countForestRiver == 0:
            forestRiver.write("""   <div id="list">""")
        
        forestRiver.write(f"""
    <div id="#rcorners3" class="panel">
        <h1 class="panel__header">{year.get()} {makeModel.get()}</h1>

        <div class="SlideHolder">
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_1.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_2.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_3.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_4.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
          <div class="{imageName}">
            <img class="panel__image" src="{imageName}_5.jpg" alt="Image of {makeModel.get()} with {extColor.get()} exterior.">
          </div>
            <a id="LeftButton" onclick="plusSlides(-1, {totalCount})">&#10094</a>
            <a id="RightButton" onclick="plusSlides(1, {totalCount})">&#10095</a>
        </div>
        
        <table class="panel__body">
            <tr>
            <td class="panel_bold">Year</td>
            <td>{year.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Miles</td>
            <td>{miles.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Engine</td>
            <td>{engine.get()}</td>
            </tr>
            <tr>
            <td class="panel_bold">Exterior Color</td>
            <td>{extColor.get()}</td>
            </tr>
        </table>
      </div>
        """)
        if countForestRiver == 2:
            forestRiver.write("""  </div>""")
            countForestRiver = 0
        else:
            countForestRiver = countForestRiver + 1
        forestRiver.close()

    totalCount = totalCount + 1
    year.delete(0, 'end')
    makeModel.delete(0, 'end')
    miles.delete(0, 'end')
    extColor.delete(0, 'end')
    VIN.delete(0, 'end')

def test():
    imageName = makeModel.get().replace(" ", "")+"_"+VIN.get()
    print(imageName)


################################################################APPEND BUTTON
addButton = tk.Button(root, text="Append to Site", command=AddtoSite)
addButton.grid(column=2, row=4)
testButton = tk.Button(root, text="test", command=CreateFiles)
testButton.grid(column=4, row=4)



##############################################################INFORMATION INPUTS
tk.Label(root, text="Enter Year: \n(YYYY) ").grid(column=0, row=0)
year = tk.Entry(root, text='Year')
year.grid(column=1, row=0)

tk.Label(root, text="Enter Make and Model: \n(Make Model) ").grid(column=0, row=1)
makeModel = tk.Entry(root, text='MakeModel')
makeModel.grid(column=1, row=1)

tk.Label(root, text="Enter Miles: \n(###,###) ").grid(column=0, row=2)
miles = tk.Entry(root, text='Miles')
miles.grid(column=1, row=2)

tk.Label(root, text="Enter Engine: \n(Automatic/Manual) ").grid(column=0, row=3)
engine = tk.Entry(root, text='Engine')
engine.grid(column=1, row=3)

tk.Label(root, text="Enter Exterior Color: \n(Black) ").grid(column=0, row=4)
extColor = tk.Entry(root, text='ExtColor')
extColor.grid(column=1, row=4, pady=4)

tk.Label(root, text="Enter VIN: \n(####) ").grid(column=2, row=0)
VIN = tk.Entry(root, text='VIN')
VIN.grid(column=3, row=0, pady=4)

###################################################################TYPE BUTTONS CHECKBOX
varAllAutos = tk.IntVar()
typeButtonAllAutos = tk.Checkbutton(root, text="All Autos", variable=varAllAutos)
typeButtonAllAutos.grid(column=0, row=5)

varCars = tk.IntVar()
typeButtonCars = tk.Checkbutton(root, text="Cars", variable=varCars)
typeButtonCars.grid(column=1, row=5)

varTrucks = tk.IntVar()
typeButtonTrucks = tk.Checkbutton(root, text="Trucks", variable=varTrucks)
typeButtonTrucks.grid(column=2, row=5)

varSUVs = tk.IntVar()
typeButtonSUVs = tk.Checkbutton(root, text="SUVs", variable=varSUVs)
typeButtonSUVs.grid(column=3, row=5)

varVans = tk.IntVar()
typeButtonVans = tk.Checkbutton(root, text="Vans", variable=varVans)
typeButtonVans.grid(column=4, row=5)

varAllCamper = tk.IntVar()
typeButtonAllCamper = tk.Checkbutton(root, text="All Camper", variable=varAllCamper)
typeButtonAllCamper.grid(column=0, row=6)

varShasta = tk.IntVar()
typeButtonShasta = tk.Checkbutton(root, text="Shasta", variable=varShasta)
typeButtonShasta.grid(column=1, row=6)

varRush = tk.IntVar()
typeButtonRush = tk.Checkbutton(root, text="Rush", variable=varRush)
typeButtonRush.grid(column=2, row=6)

varForestRiver = tk.IntVar()
typeButtonForestRiver = tk.Checkbutton(root, text="Forest River", variable=varForestRiver)
typeButtonForestRiver.grid(column=3, row=6)

root.mainloop()