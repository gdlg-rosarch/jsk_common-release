Name:           ros-jade-image-view2
Version:        2.1.2
Release:        1%{?dist}
Summary:        ROS image_view2 package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/image_view2
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-cv-bridge
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-image-geometry
Requires:       ros-jade-image-transport
Requires:       ros-jade-image-view
Requires:       ros-jade-message-filters
Requires:       ros-jade-message-runtime
Requires:       ros-jade-pcl-ros
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
Requires:       ros-jade-tf
BuildRequires:  numpy
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-geometry
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-image-view
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-pcl-ros
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-std-srvs
BuildRequires:  ros-jade-tf
BuildRequires:  scipy

%description
A simple viewer for ROS image topics with draw-on features

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
* Thu Sep 15 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.2-1
- Autogenerated by Bloom

* Wed Sep 14 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.2-0
- Autogenerated by Bloom

* Wed Sep 07 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.1-0
- Autogenerated by Bloom

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

