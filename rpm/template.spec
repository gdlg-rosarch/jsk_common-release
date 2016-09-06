Name:           ros-jade-jsk-topic-tools
Version:        2.1.0
Release:        0%{?dist}
Summary:        ROS jsk_topic_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_topic_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       numpy
Requires:       opencv-python
Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-diagnostic-updater
Requires:       ros-jade-dynamic-tf-publisher
Requires:       ros-jade-eigen-conversions
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-image-transport
Requires:       ros-jade-message-runtime
Requires:       ros-jade-nodelet
Requires:       ros-jade-roscpp
Requires:       ros-jade-roslaunch
Requires:       ros-jade-rosnode
Requires:       ros-jade-rostime
Requires:       ros-jade-rostopic
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-sound-play
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
Requires:       ros-jade-tf
Requires:       ros-jade-topic-tools
Requires:       scipy
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-diagnostic-msgs
BuildRequires:  ros-jade-diagnostic-updater
BuildRequires:  ros-jade-dynamic-tf-publisher
BuildRequires:  ros-jade-eigen-conversions
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roscpp-tutorials
BuildRequires:  ros-jade-roslaunch
BuildRequires:  ros-jade-roslint
BuildRequires:  ros-jade-rosnode
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-rostime
BuildRequires:  ros-jade-rostopic
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-std-srvs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-topic-tools

%description
jsk_topic_tools

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Tue Sep 06 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.0-0
- Autogenerated by Bloom

* Thu Jul 21 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.17-0
- Autogenerated by Bloom

* Mon Jun 20 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.16-1
- Autogenerated by Bloom

* Sun Jun 19 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.16-0
- Autogenerated by Bloom

* Tue Jun 14 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.15-0
- Autogenerated by Bloom

* Sat May 14 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.14-0
- Autogenerated by Bloom

* Fri Apr 29 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.13-0
- Autogenerated by Bloom

* Mon Apr 18 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.12-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.11-0
- Autogenerated by Bloom

* Tue Dec 15 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.9-1
- Autogenerated by Bloom

* Tue Dec 15 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.9-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.8-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.7-0
- Autogenerated by Bloom

* Thu Dec 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.6-0
- Autogenerated by Bloom

* Mon Nov 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.5-0
- Autogenerated by Bloom

* Thu Nov 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.4-2
- Autogenerated by Bloom

* Sat Aug 01 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.3-1
- Autogenerated by Bloom

* Sat Aug 01 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Tue Jul 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Sun Jun 28 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Tue Jun 23 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.0-1
- Autogenerated by Bloom

