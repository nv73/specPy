;; at_impaisa, optfile, sen_dir, raw = raw, demfile = demfile, gndalt = gndalt, fovfile = fovfile, $
;; group=group, logfile = logfile

;;For future me, $ symbol allows for multi-line functions, x = x style arguements are optional


;;THIS FUNCTION TAKES IN A .DAT HYPERSPECTRAL IMAGE EXPORTED FROM CALIGEOPRO, AND A BSQ DEM FILE
;;IT CONVERTS THE .DAT TO A .BSQ, FITS THE DEM TO IT, GENERATES THE ELEVATION, SLOPE, AND ASPECT FILES
;;THEN MAKES THE SCAN ANGLE, CALIBRATION, AND INN FILES.
;;IT THEN RUNS THE DATA THROUGH THE RUGGED ATMOSPHERIC CORRECTION ALGORITHM
PRO atcor_batch_proc, raw, dem

  restore, 'C:\Program Files (x86)\ReSe_Software_Win64\atcor_4\bin\atcor4.sav'
  
  PRINT, "Processing: "
  PRINT, raw
  
  !ATPAR.SCALEF = 1.0

  sen_dir = "C:\Program Files (x86)\ReSe_Software_Win64\atcor_4\sensor\FENIX"
  
  sen = "FENIX"
  
  fov = "C:\Program Files (x86)\ReSe_Software_Win64\atcor_4\sensor\FENIX\FOV_sn351020_20190530.txt"
  
  ele = raw.Replace(".dat", "_img_ele.bsq")

  bsq = raw.Replace(".dat", "_img.bsq")

  opt = raw.Replace("-rect.dat", ".opt")
  
  glt = raw.Replace("-rect.dat", "_GLT.dat")
  
  atm = raw.Replace(".dat", "_img_atm.bsq")
  
  sca = raw.Replace(".dat", "_sca.bsq")
  
  pol = raw.Replace(".dat", "_img_pol_atm.bsq")
  
  bcor = raw.Replace(".dat", "_img_atm_bcor.bsq")
  
  !ATF.SNS = "C:\Program Files (x86)\ReSe_Software_Win64\atcor_4\sensor\FENIX\sensor_FENIX.dat"
  
  PRINT, "Converting DAT file to BSQ..."
  
  ;bil_2_bsq, raw
  
  ;bil_2_bsq, glt
  
  PRINT, "Prepping DEM..."
  
  ;at_prepele, bsq, dem, ele, /slopasp, /skyview
    
  PRINT, "DEM prepped, generating required ASIA datasets..."
  
  ;at_impaisa, opt, sen, demfile = ele
  
  PRINT, "Running AtCor (Rugged) on data..."
  
  ;atcor4r_batch, input = !ATF.INR
  
  PRINT, "AtCor4 comeplete, running spectral polishing (Savitsky-Golay)"
  
  ;at_savpolish, atm, pol, 3

  PRINT, "Polishing complete, running brefcor BDRF corrections..."
  
  br_brefcor, atm, sca, bcor
  
END

;;Iterates through rectified dat files in a directory and runs them through
;;atcor_batch_proc
PRO batch_hsi_proc, indir, dem

  CD, indir

  dat = FILE_SEARCH("*-rect.dat")
  
  FOREACH file, dat DO atcor_batch_proc, file, dem
  
END

;;Iterates through prepared, rectified bsq files in a directory and
;;runs them through atcor4 rugged terrain corrections
PRO batch_atcor4r, indir

  CD, indir

  bsqFiles = FILE_SEARCH("*rect_img.bsq")
  
  FOREACH file, bsqFiles DO atcor4r_batch, input=file

END

