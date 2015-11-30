Name:           ros-jade-jsk-tilt-laser
Version:        2.0.5
Release:        0%{?dist}
Summary:        ROS jsk_tilt_laser package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-laser-assembler
Requires:       ros-jade-laser-filters
Requires:       ros-jade-multisense-lib
Requires:       ros-jade-robot-state-publisher
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf
Requires:       ros-jade-tf-conversions
Requires:       ros-jade-urg-node
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-laser-assembler
BuildRequires:  ros-jade-laser-filters
BuildRequires:  ros-jade-multisense-lib
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-tf-conversions

%description
The jsk_tilt_laser package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Nov 30 2015 YoheiKakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 2.0.5-0
- Autogenerated by Bloom

* Thu Nov 26 2015 YoheiKakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 2.0.4-2
- Autogenerated by Bloom

* Sat Aug 01 2015 YoheiKakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 2.0.3-1
- Autogenerated by Bloom

* Sat Aug 01 2015 YoheiKakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Tue Jul 07 2015 YoheiKakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Sun Jun 28 2015 YoheiKakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Tue Jun 23 2015 YoheiKakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 2.0.0-1
- Autogenerated by Bloom

