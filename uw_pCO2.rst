.. _pCO2:

Underway |pCO2|
===============

PIs
  * Simone Alin (NOAA/PMEL)
Technicians
  * Julian Herndon (UW/NOAA/PMEL)
  * Andrew Collins (UW/NOAA/PMEL)

The partial pressure of carbon dioxide (|pCO2|) in the surface ocean was measured throughout the cruise track of this cruise with a General Oceanics 8050 |pCO2| Measuring System.
Uncontaminated seawater was continuously passed (~1.7-2.1 L/min) through a chamber where the seawater concentration of dissolved |CO2| was equilibrated with an overlaying headspace gas.
The |CO2| mole fraction of this headspace gas (|xCO2|) was measured every two minutes via a non-dispersive infrared analyzer (LiCor 7000) for 60 consecutive measurements.
At the end of these 60 discrete measurements, a set of five standard gases was analyzed; four of these standards have known |CO2| concentrations certified by the NOAA Earth Science Research Laboratory (ESRL) ranging from ~300 to ~900 ppm |CO2| (see Table 1).
The fifth standard is a tank of 99.9995% ultra-high purity nitrogen gas, used as a baseline 0% |CO2|.
Following the measurements of standard gases, six consecutive measurements of atmospheric |xCO2| were made of air supplied through tubing fastened to the ships forward jack staff.
Twice a day, the infrared analyzer was zeroed and spanned using the nitrogen gas and the highest concentration |CO2| standard (911.41 ppm).
In addition to measurements of seawater |xCO2|, atmospheric |xCO2|, and standard gases, other variables were monitored to evaluate system performance (e.g. gas and water flow rates, pump speeds, equilibrator pressures, etc.).
For more detail on the general design and operation of this underway |pCO2| system, see [Pierrot2009]_.

Throughout the duration of the research cruise, the system performed well.
Initial problems with non-ideal water flow (i.e. <1.5 L/min) add some uncertainty to some of these measurements and will need to be carefully evaluated before determining their suitability for inclusion in the dataset (see details regarding water flow below). 
Of approximately 18,730 sea surface |xCO2| measurements, 243 have been flagged questionable (quality flag 3) and 51 have been flagged bad (quality flag 4) during this preliminary round of data quality control and assurance. 

Notes on seawater source and data:
----------------------------------

For details regarding the source of seawater to the pCO2 system, see Julian Herndon’s report from Leg One of this research cruise. 
During the first several days of this leg, substantial effort was made by research technicians and the chief engineer to establish sufficient water flow to the system. 
Initial efforts included trying to balance the water flow to meet the needs of the various (i.e. biological, chemical, shipboard) users onboard. 
However, insufficient flow persisted to the |pCO2| system. 
Flow was increased by closing down a forward overflow drain, but quickly dropped below 1.5 L/min. 
After exhausting nearly every possible avenue by balancing flows, adjusting pump speeds and pressures, it was determined that an obstruction must be preventing sufficient flow to the system. 
John Ballard and Andrew Collins disassembled the primary equilibrator in the |pCO2| system to learn that it was indeed obstructed. 
After cleaning, the flow to the |pCO2| system was greatly enhanced and remained sufficient for the remainder of the cruise. 
No other major problems were encountered during the cruise that affected data quality. 
One issue that persists relates to occasional dropouts from the MET system, likely due to a timing mismatch in the communications setup.

The Resident Technicians onboard used bleach to clean/sanitize the scientific seawater system after we departed Hawaii and prior to the |pCO2| system being turned on. 
Model and serial numbers for the |pCO2| instrument components and ancillary instruments have been recorded in a separate Excel file and will reported as part of the metadata that will accompany the final/processed |pCO2| data submission. 
This |pCO2| system does not have a Druck or other external barometer installed in the dry box to measure the pressure in the LiCor cell. 
The primary equilibrator in this |pCO2| system is an older, non-jacketed equilibrator built using a clear plastic filter housing.

To facilitate data processing and future troubleshooting of the Revelle |pCO2| system, the column headings for data in the |pCO2| files sourced from the ship are identified in Table #2. 
Serial numbers and additional details for the instruments in table #2 are in a separate excel file and will be reported as part of the metadata for |pCO2| data submitted from this cruise.

.. csv-table:: Table 1: Standard gases for P02 2022 cruise UW |pCO2| system.
   :header: Standard	,Concentration (ppm),Tank Serial Numbers

   1,0.0,Praxair 5.0 Ultra High Purity N2
   2,283.42,LL55868
   3,399.51,LL127199
   4,539.97,LL127204
   5,911.41,LL127176

.. csv-table:: Table 2: |pCO2| system ship supplied data column headers for P02 2022 cruise, Leg 1.  MWL = mean water level.
   :header: Column Header, Instrument, System, Location

   TSGF1,SW flow meter,3,Bow
   TSGT2,TSG45 temperature,2 and 3,Hydrolab
   TSGS2,TSG45 salinity,2 and 3,Hydrolab
   TSGF2,SW flow meter to TSG45,2 and 3,Hydrolab
   PCO2F,SW flow meter to |pCO2|,2 and 3,Hydrolab
   SST,SBE 38 temperature,3,Bow
   AT,RM Young temperature,MET,56’ above MWL*
   BP,RM Young barometer,MET,56’ above MWL*
   HDG,Konsberg GPS,,
   SOG,Speed over ground,,

While the raw data is not reported here, it has been collected and will be analyzed using MATLAB® routines developed by Dr. Denis Pierrot of the Atlantic Oceanographic and Meteorological Lab in Miami, FL. 
Measurements of gas standards were generally within 1% of their certified value throughout the duration of the cruise. 

The data from the |pCO2| system that is included as part of the ships data supplied by the onboard Resident Technicians is |xCO2| (not |pCO2|) that has not been processed or evaluated for QA/QC and as such should be considered preliminary.


.. [Pierrot2009] Pierrot, D., Neill, C., Sullivan, K., Castle, R., Wanninkof, R.W., Lüger, H., Johannessen, T., Olsen, A., Feely, R.A., Cosca, C.E.;
    2009. Recommendations for autonomous underway pCO2 measuring systems and data-reduction routines. Deep-Sea Research II 56 (2009) 512–522 
