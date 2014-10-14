Name:           ros-hydro-image-view2
Version:        1.0.49
Release:        0%{?dist}
Summary:        ROS image_view2 package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/image_view2
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-image-geometry
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-image-view
Requires:       ros-hydro-message-filters
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-pcl-ros
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-tf
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-image-geometry
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-image-view
BuildRequires:  ros-hydro-message-filters
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-pcl-ros
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-tf

%description
A simple viewer for ROS image topics with draw-on features

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir build && cd build
cmake .. \
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
cd build
make install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Oct 14 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.49-0
- Autogenerated by Bloom

* Sun Oct 12 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.48-0
- Autogenerated by Bloom

