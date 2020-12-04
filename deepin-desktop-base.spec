Name:           deepin-desktop-base
Version:        2020.03.23
Release:        2
Summary:        Base files for Deepin Desktop
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-desktop-base
Source0:        %{name}_%{version}.orig.tar.xz	
BuildArch:      noarch
Patch1:         0001-fix-logo.patch 

Provides: deepin-appstore-config

%description
Base files for Deepin Desktop.

%package       -n deepin-desktop-server
Summary:       Base files for Deepin Desktop
Requires:      deepin-keyring distro-info-data eject fonts-noto fonts-symbola


%description   -n deepin-desktop-server
Base files for Deepin Desktop.

%prep
%autosetup -p1

sed -i -E '/lsb-release/d' Makefile
sed -i 's|/usr/lib|%{_datadir}|' Makefile
sed -i 's|VERSION := 20 SP1|VERSION := 20|' Makefile
sed -i 's|Type=.*|Type=Server-Euler|' files/desktop-version-arm.in
sed -i 's|Type\[zh_CN\]=.*|Type\[zh_CN\]=服务器欧拉版|' files/desktop-version-arm.in

%build
%make_build

%install
install -d -p %{buildroot}/%{_datadir}/i18n
install -d -p %{buildroot}/%{_datadir}/python-apt/templates
install -d -p %{buildroot}/%{_datadir}/deepin/distribution/
install -d -p %{buildroot}/%{_sysconfdir}/deepin

install -Dm644 files/i18n_dependent.json  %{buildroot}/%{_datadir}/i18n/i18n_dependent.json
install -Dm644 files/language_info.json   %{buildroot}/%{_datadir}/i18n/language_info.json
install -Dm644 files/logind.conf   %{buildroot}/%{_sysconfdir}/systemd/logind.conf.d/logind.conf
install -Dm644 files/systemd.conf  %{buildroot}/%{_sysconfdir}/systemd/system.conf.d/systemd.conf
install -Dm644 files/desktop-version-server %{buildroot}/usr/lib/deepin/desktop-version-server
install -Dm644 files/desktop-version %{buildroot}%{_datadir}/deepin/desktop-version
install -Dm644 files/appstore.json     %{buildroot}/%{_sysconfdir}/appstore.json
install -Dm644 files/dde-session-ui.conf %{buildroot}/%{_sysconfdir}/deepin/dde-session-ui.conf
install -Dm644 files/deepin-logo.png   %{buildroot}/%{_datadir}/plymouth/deepin-logo.png
install -Dm644 files/uos_logo.svg      %{buildroot}/%{_datadir}/deepin/uos_logo.svg
install -Dm644 distribution.info       %{buildroot}/%{_datadir}/deepin/distribution.info
install -Dm644 distribution/*.svg      %{buildroot}/%{_datadir}/deepin/distribution/
install -Dm644 files/Deepin.info    %{buildroot}/%{_datadir}/python-apt/templates/Deepin.info
install -Dm644 files/Deepin.mirrors %{buildroot}/%{_datadir}/python-apt/templates/Deepin.mirrors
install -Dm644 files/dde-desktop-watermask.json     %{buildroot}/%{_datadir}/deepin/dde-desktop-watermask.json
[ -e files/systemd.conf ] && install -Dm644 files/systemd.conf %{buildroot}/%{_sysconfdir}/systemd/system.conf.d/deepin-base.conf
[ -e files/logind.conf ] && install -Dm644 files/logind.conf   %{buildroot}/%{_sysconfdir}/systemd/logind.conf.d/deepin-base.conf


ln -sfv ..%{_datadir}/deepin/desktop-version %{buildroot}/etc/deepin-version

%files
%config(noreplace) %{_sysconfdir}/appstore.json
%{_sysconfdir}/deepin-version
%dir %{_datadir}/deepin/
%{_sysconfdir}/systemd/logind.conf.d/logind.conf
%{_sysconfdir}/systemd/system.conf.d/systemd.conf
%{_sysconfdir}/systemd/logind.conf.d/deepin-base.conf
%{_sysconfdir}/systemd/system.conf.d/deepin-base.conf
%{_datadir}/deepin/desktop-version
%{_datadir}/i18n/i18n_dependent.json
%{_datadir}/i18n/language_info.json
%dir %{_datadir}/plymouth
%{_datadir}/plymouth/deepin-logo.png
%{_datadir}/python-apt/templates/Deepin.info
%{_datadir}/python-apt/templates/Deepin.mirrors
%{_datadir}/deepin/dde-desktop-watermask.json
%{_datadir}/deepin/uos_logo.svg
%{_datadir}/deepin/distribution.info
%{_datadir}/deepin/distribution/distribution_logo.svg
%{_datadir}/deepin/distribution/distribution_logo_light.svg
%{_datadir}/deepin/distribution/distribution_logo_transparent.svg

%files -n deepin-desktop-server
%config(noreplace) %{_sysconfdir}/appstore.json
%config(noreplace) %{_sysconfdir}/deepin/dde-session-ui.conf
/usr/lib/deepin/desktop-version-server
%dir %{_datadir}/deepin/
%{_sysconfdir}/systemd/logind.conf.d/logind.conf
%{_sysconfdir}/systemd/system.conf.d/systemd.conf
%{_sysconfdir}/systemd/logind.conf.d/deepin-base.conf
%{_sysconfdir}/systemd/system.conf.d/deepin-base.conf
%{_datadir}/deepin/desktop-version
%{_datadir}/i18n/i18n_dependent.json
%{_datadir}/i18n/language_info.json
%dir %{_datadir}/plymouth
%{_datadir}/plymouth/deepin-logo.png
%{_datadir}/python-apt/templates/Deepin.info
%{_datadir}/python-apt/templates/Deepin.mirrors
%{_datadir}/deepin/dde-desktop-watermask.json
%{_datadir}/deepin/uos_logo.svg
%{_datadir}/deepin/distribution.info
%{_datadir}/deepin/distribution/distribution_logo.svg
%{_datadir}/deepin/distribution/distribution_logo_light.svg
%{_datadir}/deepin/distribution/distribution_logo_transparent.svg

%changelog
* Sat Dec 05 2020 weidong <weidong@uniontech.com> - 2020.03.23-2
- fix logo

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 2020.03.23-1
- Package init
