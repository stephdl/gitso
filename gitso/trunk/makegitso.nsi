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
  VIProductVersion "0.5.0.0"
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
  ;need to add gitso's exe file here after created with py2exe or something like it
  SetOutPath $WINDIR
  File ".\arch\win32\vncviewer.exe"
  File ".\arch\win32\WinVNC.exe"
  File ".\arch\win32\VNCHooks.dll"
  CreateShortCut "$INSTDIR\gitso.exe" "$INSTDIR\gitso.exe" "" "$INSTDIR\gitso.exe" 0
  WriteRegDWORD HKCU "Software\ORL\WinVNC3" "RemoveWallpaper" 1
  WriteRegDWORD HKCU "Software\ORL\WinVNC3" "EnableFileTransfers" 1
 ;set default password to something so WinVNC.exe doesn't complain about having no password
  WriteRegBin HKCU "SOFTWARE\ORL\WinVNC3" "Password" "238f16962aeb734e"
  WriteRegBin HKCU "SOFTWARE\ORL\WinVNC3" "PasswordViewOnly" "b0f0ac1997133bc9"
 ;Try to set it for all users, but I'm not positive this works
  WriteRegDWORD HKLM "Software\ORL\WinVNC3" "RemoveWallpaper" 1
  WriteRegDWORD HKLM "Software\ORL\WinVNC3" "EnableFileTransfers" 1
  WriteRegBin HKLM "SOFTWARE\ORL\WinVNC3" "Password" "238f16962aeb734e"
  WriteRegBin HKLM "SOFTWARE\ORL\WinVNC3" "PasswordViewOnly" "b0f0ac1997133bc9"
SectionEnd


; Uninstall
;------------------------------------------------------
Section "Uninstall"
  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\RMTT"
  DeleteRegKey HKLM SOFTWARE\RMTT
  ; Remove files and uninstaller
  Delete $WINDIR\vncviewer.exe
  Delete $WINDIR\VNCHooks.dll
  Delete $WINDIR\WinVNC.exe
  Delete $INSTDIR\gitso.exe
  RMDir /r $INSTDIR
  Delete $INSTDIR\uninstall.exe
  Delete "$DESKTOP\RMTT.lnk"
  ; Remove shortcuts and folder
  RMDir /r "$SMPROGRAMS\RMTT"
  RMDir "$INSTDIR"
SectionEnd
