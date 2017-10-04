Name:           ros-kinetic-jsk-tools
Version:        2.2.5
Release:        0%{?dist}
Summary:        ROS jsk_tools package

Group:          Development/Libraries
License:        Apache License 2.0
URL:            http://ros.org/wiki/jsk_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       iproute
Requires:       python-colorama
Requires:       python-requests
Requires:       python-texttable
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-jsk-gui-msgs
Requires:       ros-kinetic-jsk-network-tools
Requires:       ros-kinetic-jsk-topic-tools
Requires:       ros-kinetic-rosbag
Requires:       ros-kinetic-rosemacs
Requires:       ros-kinetic-rosgraph-msgs
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rqt-reconfigure
BuildRequires:  git
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-rosgraph-msgs
BuildRequires:  ros-kinetic-roslint
BuildRequires:  ros-kinetic-rostest

%description
Includes emacs scripts, ros tool alias generator, and launch doc generator.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Oct 04 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.2.5-0
- Autogenerated by Bloom

* Thu Jan 12 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.2.2-0
- Autogenerated by Bloom

* Sat Oct 22 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.2-1
- Autogenerated by Bloom

