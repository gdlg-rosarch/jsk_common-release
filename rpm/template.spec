Name:           ros-indigo-jsk-network-tools
Version:        2.1.2
Release:        0%{?dist}
Summary:        ROS jsk_network_tools package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs

%description
jsk_network_tools

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Sep 14 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.2-0
- Autogenerated by Bloom

* Wed Sep 07 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.1-0
- Autogenerated by Bloom

* Tue Sep 06 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.0-0
- Autogenerated by Bloom

* Thu Jul 21 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.17-0
- Autogenerated by Bloom

* Sun Jun 19 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.16-1
- Autogenerated by Bloom

* Sun Jun 19 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.16-0
- Autogenerated by Bloom

* Tue Jun 14 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.15-1
- Autogenerated by Bloom

* Mon Jun 13 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.15-0
- Autogenerated by Bloom

* Sat May 14 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.14-0
- Autogenerated by Bloom

* Fri Apr 29 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.13-0
- Autogenerated by Bloom

* Mon Apr 18 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.12-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.11-0
- Autogenerated by Bloom

* Tue Dec 15 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.9-1
- Autogenerated by Bloom

* Tue Dec 15 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.9-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.8-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.7-0
- Autogenerated by Bloom

* Thu Dec 03 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.6-0
- Autogenerated by Bloom

* Mon Nov 30 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.5-0
- Autogenerated by Bloom

* Wed Nov 25 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.4-1
- Autogenerated by Bloom

* Fri Jul 24 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Tue Jul 07 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Sun Jun 28 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom

* Mon May 18 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.71-0
- Autogenerated by Bloom

* Sat May 09 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.70-1
- Autogenerated by Bloom

* Sat May 09 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.70-0
- Autogenerated by Bloom

* Tue May 05 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.69-0
- Autogenerated by Bloom

* Tue May 05 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.68-0
- Autogenerated by Bloom

* Mon May 04 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.67-0
- Autogenerated by Bloom

* Fri Apr 03 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.66-0
- Autogenerated by Bloom

* Thu Apr 02 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.65-0
- Autogenerated by Bloom

* Wed Apr 01 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.64-0
- Autogenerated by Bloom

* Thu Feb 19 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.63-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.62-0
- Autogenerated by Bloom

* Wed Feb 11 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.61-0
- Autogenerated by Bloom

* Wed Feb 04 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.60-1
- Autogenerated by Bloom

* Tue Feb 03 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.60-0
- Autogenerated by Bloom

* Tue Feb 03 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.59-1
- Autogenerated by Bloom

* Tue Feb 03 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.59-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.58-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.57-0
- Autogenerated by Bloom

* Wed Dec 17 2014 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.56-0
- Autogenerated by Bloom

* Wed Dec 10 2014 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.55-1
- Autogenerated by Bloom

* Tue Dec 09 2014 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.55-0
- Autogenerated by Bloom

* Sat Nov 15 2014 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.54-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.53-0
- Autogenerated by Bloom

* Sun Oct 12 2014 Yusuke Furuta <furuta@jsk.imi.i.u-tokyo.ac.jp> - 1.0.48-0
- Autogenerated by Bloom

