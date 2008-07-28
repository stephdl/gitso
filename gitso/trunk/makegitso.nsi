; gitso.nsi
; ----------------
; written by Derek Buranen (xburnerx@gmail.com) & Aaron Gerber
; 
; Install Gitso in Windows using NSIS
;--------------------------------

!define VERSION "0.5" 
Name "Gitso ${VERSION}"
Icon "icon.ico"
UninstallIcon "icon.ico"
OutFile "gitso-install.exe"

; The default installation directory
InstallDir $PROGRAMFILES\Gitso
; Registry key to check for directory (so if you install again, it will overwrite the old one automatically)
InstallDirRegKey HKLM "Software\Gitso" "Install_Dir"

;--------------------------------
; Version Information
  VIProductVersion "0.0.0.0"
  VIAddVersionKey "ProductName" "Gitso"
  VIAddVersionKey "Comments" "Gitso is to support others"
  VIAddVersionKey "CompanyName" "http://code.google.com/p/gitso"
  VIAddVersionKey "LegalCopyright" "GPL"
  VIAddVersionKey "FileDescription" "Gitso"
  VIAddVersionKey "FileVersion" "${VERSION}"
;--------------------------------

;--------------------------------
; Pages
Page components
Page directory
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles
;--------------------------------

Section "Gitso"
  SectionIn RO
  SetOutPath $INSTALLDIR
  File ".\icon.ico"
  File ".\hosts.txt"
  File ".\Gitso.py"
  ;need to add gitso's exe file here after created with py2exe or something like it
  SetOutPath $WINDIR
  File ".\arch\win32\vncviewer.exe"
  File ".\arch\win32\WinVNC.exe"
  File ".\arch\win32\VNCHooks.dll"
SectionEnd


; Uninstall
;------------------------------------------------------
Section "Uninstall"
  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\RMTT"
  DeleteRegKey HKLM SOFTWARE\RMTT
  ; Remove files and uninstaller
  Delete $WINDIR\revealer.dll
  Delete $WINDIR\revealer.exe
  Delete $WINDIR\Startup.exe
  Delete $WINDIR\VNCHooks.dll
  Delete $WINDIR\WinVNC.exe
  RMDir /r $INSTDIR
  Delete $INSTDIR\uninstall.exe
  Delete "$DESKTOP\RMTT.lnk"
  Delete "$WINDIR\Tasks\Spyware Scan.job"
  ; Remove shortcuts and folder
  RMDir /r "$SMPROGRAMS\RMTT"
  RMDir "$INSTDIR"
SectionEnd

