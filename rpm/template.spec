Name:           ros-jade-jsk-common
Version:        2.0.1
Release:        0%{?dist}
Summary:        ROS jsk_common package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-dynamic-tf-publisher
Requires:       ros-jade-image-view2
Requires:       ros-jade-jsk-network-tools
Requires:       ros-jade-jsk-tilt-laser
Requires:       ros-jade-jsk-tools
Requires:       ros-jade-jsk-topic-tools
Requires:       ros-jade-multi-map-server
Requires:       ros-jade-virtual-force-publisher
BuildRequires:  ros-jade-catkin

%description
Metapackage that contains commonly used toolset for jsk-ros-pkg

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
* Sun Jun 28 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Tue Jun 23 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.0-1
- Autogenerated by Bloom

