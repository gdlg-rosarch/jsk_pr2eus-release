Name:           ros-kinetic-pr2eus-tutorials
Version:        0.3.10
Release:        0%{?dist}
Summary:        ROS pr2eus_tutorials package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2eus_tutorials
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-jsk-pcl-ros
Requires:       ros-kinetic-pr2eus
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-jsk-pcl-ros
BuildRequires:  ros-kinetic-pr2eus

%description
pr2eus_tutorials

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
* Thu Mar 02 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.10-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.9-1
- Autogenerated by Bloom

