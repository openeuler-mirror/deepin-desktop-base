%global         debug_package %{nil}

Name:           deepin-desktop-base
Version:        2021.05.24
Release:        3
Summary:        Base files for Deepin Desktop
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-desktop-base
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-fix-logo.patch
Patch1000:      1000-add-riscv64-support.patch

%description
%{summary}.

%package        -n deepin-desktop-server
Summary:        Base files for Deepin Desktop Server
Provides:       deepin-desktop-base
Obsoletes:      deepin-desktop-base < %{version}
Recommends:     deepin-wallpapers
Recommends:     deepin-screensaver

%description    -n deepin-desktop-server
%{summary}.


%prep
%autosetup -p1

%build
# Remove Deepin lsb-release
sed -i '/lsb-release/d' Makefile
# update usr/lib/ path
sed -i 's|/usr/lib|%{_datadir}|' Makefile
# 社区版
sed -i 's|Type\[zh_CN\]=.*|Type\[zh_CN\]=社区版|' files/{desktop-version-arm-server.in,desktop-version-server.in,desktop-version.in}
sed -i 's|Edition=.*|Edition=Y2020E0001|' files/{desktop-version-arm-server.in,desktop-version-server.in,desktop-version.in}
sed -i 's|Copyright=.*|Copyright=Y2020CR001|' files/{desktop-version-arm-server.in,desktop-version-server.in,desktop-version.in}
%make_build

%install
%make_install
## install distribution.info
install -d -p %{buildroot}/%{_datadir}/deepin/distribution/
install -Dm644 distribution.info       %{buildroot}/%{_datadir}/deepin/distribution.info
install -Dm644 distribution/*.svg      %{buildroot}/%{_datadir}/deepin/distribution/
install -Dm644 files/logind.conf   %{buildroot}/%{_sysconfdir}/systemd/logind.conf.d/logind.conf
install -Dm644 files/systemd.conf  %{buildroot}/%{_sysconfdir}/systemd/system.conf.d/systemd.conf
install -Dm644 files/dde-session-ui.conf  %{buildroot}/etc/deepin/dde-session-ui.conf
install -Dm644 files/desktop-version-server %{buildroot}%{_datadir}/deepin/desktop-version-server
ln -sfv %{_datadir}/deepin/desktop-version-server %{buildroot}%{_sysconfdir}/deepin-version
#install -Dm644 files/os-license %{buildroot}/%{_sysconfdir}/.uos/os-license

%files -n deepin-desktop-server
%{_sysconfdir}/deepin-version
%{_datadir}/i18n/*.json
%{_datadir}/deepin/distribution.info
%{_datadir}/deepin/distribution/
%{_datadir}/deepin/desktop-version-server
%{_sysconfdir}/appstore.json
%{_datadir}/plymouth/deepin-logo.png
%{_datadir}/deepin/uos_logo.svg
%{_sysconfdir}/systemd/system.conf.d/systemd.conf
%{_sysconfdir}/systemd/logind.conf.d/logind.conf
%{_datadir}/python-apt/templates/Deepin.info
%{_datadir}/python-apt/templates/Deepin.mirrors
%{_datadir}/deepin/dde-desktop-watermask.json
%{_sysconfdir}/deepin/dde-session-ui.conf
%exclude %{_sysconfdir}/systemd/logind.conf.d/deepin-base.conf
%exclude %{_sysconfdir}/systemd/system.conf.d/deepin-base.conf
%exclude %{_sysconfdir}/systemd/user.conf.d/deepin-base.conf
%exclude %{_datadir}/deepin/desktop-version
# conflicts with file from package license-config
%exclude %{_localstatedir}/uos/os-license
%exclude %{_sysconfdir}/os-version

%changelog
* Thu Aug 11 2022 misaka00251 <misaka00251@misakanet.cn> - 2021.05.24-4
- Merge upstream & fix riscv64 support

* Fri Aug 05 2022 liweiganga <liweiganga@uniontech.com> - 2021.05.24-3
- fix version type

* Tue Aug 02 2022 liweiganga <liweiganga@uniontech.com> - 2021.05.24-2
- Modified to Community Edition

* Mon Jul 18 2022 konglidong <konglidong@uniontech.com> - 2021.05.24-1
- update to 2021.05.24

* Fri Jun 10 2022 misaka00251 <misaka00251@misakanet.cn> - 2020.09.11-3
- Add riscv64 support

* Thu Aug 26 2021 konglidong <konglidong@uniontech.com - 2020.09.11-2
- Fix versions
- Fix logos error

* Tue Jul 20 2021 weidong <weidong@uniontech.com> - 2020.09.11-1
- Update 2020.09.11

* Sat Jun 05 2021 weidong <weidong@uniontech.com> - 2020.03.23-4
- Fix installation dependency errors

* Tue Feb 23 2021 weidong <weidong@uniontech.com> - 2020.03.23-3
- Update deepin-version 

* Sat Dec 05 2020 weidong <weidong@uniontech.com> - 2020.03.23-2
- fix logo

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 2020.03.23-1
- Package init
