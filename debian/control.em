Source: @(Package)
Section: misc
Priority: extra
Maintainer: @(Maintainer)
Build-Depends: debhelper (>= @(debhelper_version).0.0), @(', '.join(BuildDepends))
@[if Conflicts]Conflicts: @(', '.join(Conflicts))@\n@[end if]
@[if Replaces]Replaces: @(', '.join(Replaces))@\n@[end if]
Homepage: @(Homepage)
Standards-Version: 3.9.2

Package: @(Package)
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}, @(', '.join(Depends))
Description: @(Description)
