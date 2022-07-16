LADCP
=====

PI
  * Dr. Andreas Thurnherr (LDEO)
Cruise Participant
  * Lily Dove (Caltech)

Data Acquisition and QC
-----------------------
In order to collect full-depth profiles of horizontal and vertical ocean velocity, two Acoustic Doppler Current Profilers (ADCPs), one facing upward (uplooker, UL) and the other downward (downlooker, DL), as well as a Deep Sea Power And Light rechargeable 48V battery and cables were installed on the CTD rosette.
This lowered ADCP (LADCP) system was provided by the Lamont-Doherty Earth Observatory (LDEO).
The LADCP system is self-contained, requiring on-deck cable connections to charge the battery and for communicating with the ADCPs. 
The battery charger was affixed to an elevated cable run in the CTD bay with an extension power cable run into the wet lab to be plugged in near to the hanger door. 
The LADCP data acquisition computer, a Mac Mini, as well as a bench-top power supply for the ADCPs were installed on the bench.

Between casts, the LADCP system in the CTD bay was left connected to the (unpowered) battery charger, as well as to the two deck cables leading to the data acquisition computer and to the bench-top power supply. 
The plug of the (disconnected) adapter cable between the battery and the LADCP star cable was dummied. 
While the deck cables in the wet lab were permanently connected to the acquisition computer with RS232-to-USB adapters, the corresponding power connectors were left disconnected from the bench-top power supplies. 
With this setup there is no voltage on any of the LADCP cables on the rosette.

A few minutes before the CTD rosette was moved out of the hanger for deployment, the battery was disconnected from the charger and connected to the ADCPs via an adapter cable and the star cable, both of which were permanently installed on the rosette. 
The plug of the battery charger cable was dummied. 
To start data acquisition, the instruments were woken up by the acquisition computer, the data from the previous cast deleted from their built-in memory cards, and the instruments programmed to start pinging. 
Finally, the two deck cables were disconnected from the two star-cable extensions. 
The deck cables and pig-tail connectors were dummied and the latter were secured to the rosette with a Velcro strap to avoid excessive motion during the casts. 
Once everything was set up, the CTD operator and the ResTech were notified that the LADCP system was ready for deployment. 
Deployment information was logged on LADCP log sheets once the rosette had entered the water.

After the CTD had been secured in the bay following each cast, the Velcro securing the dummied pig-tail ends to the rosette was removed, the dummy plugs were removed, and the pig tails were rinsed with fresh water and connected to the deck cables. 
Using the acquisition computer, LADCP data acquisition was stopped and the data download was initiated. 
The bench top power supply was connected to the deck cables in the lab, the battery was disconnected from the adapter cable on the rosette, the plug of the battery adapter cable on the rosette with two exposed pins now carrying 48V (from the bench-top power supply) was dummied, and the battery cable was attached to the (still unpowered) charger cable. 
Afterwards, power was applied to the battery charger via an accessible power toggle switch below the charger and the time noted on the LADCP log sheet.

After the data from the cast had finished downloading (after about 20 minutes for deep casts, 5 minutes for bio casts), the bench top power supply was deactivated with a power toggle switch. 
Then the data files, one for each the UL and DL, were checked by integrating the measured vertical velocities in time, which yields estimates for the maximum depth (zmax) and the end depth (zend) of the profile, both of which were recorded on the log sheet. 
After the battery was fully charged (usually about an hour after charging was initiated, as indicated by LEDs on the charger) the charger was disconnected from power in the wet lab and the time was noted on the log sheet. 
At this stage, the LADCP system was ready for the next cast.

Communication between the acquisition computer and the ADCPs was handled by a new acquisition software (acquire2), implemented as a set of UNIX shell commands designed to minimize the possibility of operator errors. 
Three different commands are used:


*Ldir*: Lists the status of the LADCP memory, including number of files, file size, etc.
Used to ensure the LADCP is operational while connected to the bench power.

*Lstart*: Wakes the instruments, lists their memory contents, clears the memory (after operator confirmation) and programs the instruments to start pinging by uploading command files.
CTD station and cast numbers must be provided by the operator since the LADCP files use an independent numbering scheme.

*Ldownload*: Interrupts the running data acquisition, downloads the data, and backs up the data files to a network drive.

*Lcheck*: Integrates the measured vertical velocities from both ADCPs to estimate zmax and zend, which are displayed together with other useful profile statistics before the data files are backed up on the network drive.

While these three commands are all that is needed for LADCP data acquisition, a fourth command (*Lreset*) is available for resetting the ADCPs after swapping instruments and in case of communications problems.

During the night watch, the LADCP data were processed for horizontal velocity using the LDEO_IX processing software and for vertical velocity using the LADCP_w processing software, both installed on the acquisition computer and accessed on a personal computer using Screen Sharing. 
CTD .cnv data were obtained from the ship’s shared drive and processed into 1 and 6 Hz formats using the LADCP_w processing software. 
In addition to the zend and zmax processing diagnostics, LADCP data quality was monitored by creating section plots, seen in Figure 1. 
Over most of the section the LADCP data quality appears to be good, although the lack of backscattering particles throughout the intermediate and abyssal depths of the water column off the shelf lead to potentially unconstrained velocities. 
A more comprehensive post-cruise LADCP QC will be carried out by Thurnherr in his lab before submission of the combined P02 leg 1 and 2 data to the archives. 

Instrumentation
----------------

Two 300kHz Teledyne RDI Workhorse Monitor ADCPs (WHM300HZ) were used: a primary/DL (S/N 3441) and secondary/UL (S/N 12734). 
The UL instrument replaced another instrument used on leg 1 (S/N 754) before any profiles began on leg 2. 
The replacement UL (S/N 12734) was fitted with a custom self-recording accelerometer/magnetometer package. 
The data from the accelerometer/magnetometer package will be downloaded after the instruments return to the lab and used for QC and final processing if needed. 
The secondary instrument is synced to the primary instrument to follow a staggered ping rate of 1.3 and 1.6 seconds, designed to mitigate acoustic reflection depth issues. 
Data quality for the duration of the cruise is generally good, with both instruments working well.

After cast 204, the final cast of the official P02 transect, the DL instrument was replaced with a different instrument (S/N 24477), also fitted with a custom self-recording accelerometer/ magnetometer package. 
This DL was used for the remainder of the stations. 
The Deep Sea Power And Light rechargeable 48V battery (S/N 1223) experienced no problems with charging or operation over the duration of the cruise.


Preliminary Results
-------------------

ADCPs rely on particles, such as marine life and sinking detritus, in the water column in order to measure the current. The measure of particles in the water is called backscatter. Backscatter is variable across the global ocean and throughout the water column. Figure 2 shows the backscatter from Leg 2 of P02. Note the double layer of backscatter in the upper 1000 meters from station 11801 to station 18401. There is also a significant increase in backscatter at intermediate and abyssal depths near the coast (stations 18901 onwards). Regions with low backscatter make it difficult to constrain the calculated horizontal velocities, so further quality control is needed in the intermediate and abyssal depths of the first part of Leg 2.

There are three “boundary conditions” imposed on the calculation of horizontal velocities from the LADCP: the GPS, the bottom track, and the shipboard ADCP (SADCP). Figure 3 shows the root mean squared error [m/s] from the removal of the bottom track and SADCP from calculations of the horizontal velocities. Note the decrease of error upon approach to the shelf (past station 18401), likely as a result of increased backscatter.

Figures
-------

.. figure:: images/LADCP/uv_velocities.*

  Figure 1: (a) Zonal (east-west) and (b) meridional (north-south) velocities calculated from the LADCP across the full Leg 2 of P02.

.. figure:: images/LADCP/backscatter.*

  Figure 2: Backscatter [decibels] along the P02 Leg 2 transect. The colorbar is designed so each block of color contains an equal number of points.

.. figure:: images/LADCP/RMSE.*

  Figure 3: Root mean squared error [m/s] resulting from the removal of the bottom track (blue) and shipboard ADCP (orange) boundary conditions.
