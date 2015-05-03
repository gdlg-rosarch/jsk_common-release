Name:           ros-hydro-collada-urdf-jsk-patch
Version:        1.0.67
Release:        0%{?dist}
Summary:        ROS collada_urdf_jsk_patch package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/collada_urdf_jsk_patch
Source0:        %{name}-%{version}.tar.gz

Requires:       collada-dom-devel
Requires:       gts
Requires:       ros-hydro-angles
Requires:       ros-hydro-assimp-devel
Requires:       ros-hydro-class-loader
Requires:       ros-hydro-collada-parser
Requires:       ros-hydro-collada-urdf
Requires:       ros-hydro-geometric-shapes
Requires:       ros-hydro-kdl-parser
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-resource-retriever
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-tf
Requires:       ros-hydro-urdf
BuildRequires:  collada-dom-devel
BuildRequires:  git
BuildRequires:  gts
BuildRequires:  ros-hydro-angles
BuildRequires:  ros-hydro-assimp-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-class-loader
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-collada-parser
BuildRequires:  ros-hydro-collada-urdf
BuildRequires:  ros-hydro-geometric-shapes
BuildRequires:  ros-hydro-kdl-parser
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-resource-retriever
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-tf

%description
unaccepted patch for collada_urdf

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon May 04 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.67-0
- Autogenerated by Bloom

* Fri Apr 03 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.66-0
- Autogenerated by Bloom

* Thu Apr 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.65-0
- Autogenerated by Bloom

* Wed Apr 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.64-0
- Autogenerated by Bloom

* Thu Feb 19 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.63-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.62-0
- Autogenerated by Bloom

* Wed Feb 11 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.61-0
- Autogenerated by Bloom

* Wed Feb 04 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.60-1
- Autogenerated by Bloom

* Tue Feb 03 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.60-0
- Autogenerated by Bloom

* Tue Feb 03 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.59-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.58-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.57-0
- Autogenerated by Bloom

* Sun Dec 21 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.56-0
- Autogenerated by Bloom

* Tue Dec 09 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.55-0
- Autogenerated by Bloom

* Sat Nov 15 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.54-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.53-0
- Autogenerated by Bloom

* Mon Oct 20 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.51-0
- Autogenerated by Bloom

* Tue Oct 14 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.49-0
- Autogenerated by Bloom

* Sun Oct 12 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.48-0
- Autogenerated by Bloom

