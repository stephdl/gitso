; gitso.nsi
; ----------------
; written by Derek Buranen (xburnerx@gmail.com) & Aaron Gerber
; 
; Package Gitso for Windows using NSIS
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
  File ".\dist\Gitso.exe"
  File ".\dist\bz2.pyd"
  File ".\dist\icon.ico"
  File ".\dist\library.zip"
  File ".\dist\msvcp71.dll"
  File ".\dist\MSVCR71.dll"
  File ".\dist\python25.dll"
  File ".\dist\unicodedata.pyd"
  File ".\dist\w9xpopen.exe"
  File ".\dist\wx._controls_.pyd"
  File ".\dist\wx._core_.pyd"
  File ".\dist\wx._gdi_.pyd"
  File ".\dist\wx._misc_.pyd"
  File ".\dist\wx._windows_.pyd"
  File ".\dist\wxbase28uh_net_vc.dll"
  File ".\dist\wxbase28uh_vc.dll"
  File ".\dist\wxbase28uh_adv_vc.dll"
  File ".\dist\wxbase28uh_core_vc.dll"
  File ".\dist\wxbase28uh_html_vc.dll"
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
