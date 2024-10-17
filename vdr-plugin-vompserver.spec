
%define plugin	vompserver
%define name	vdr-plugin-%plugin
%define version	0.3.1
%define rel	2

Summary:	VDR plugin: VDR on MVP plugin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		https://www.loggytronic.com/vomp.php
Source:		http://www.loggytronic.com/dl/vdr-%plugin-%version.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
VOMP brings Video Disk Recorder (VDR) functionality to other
devices. There is a plugin for VDR and client software for the
Hauppauge MVP and now also Windows. The clients talk to the server
over a network. The original idea was to make a clean set-top-box
out of the MVP with an easy user interface much like a normal
digital TV consumer set-top-box. 

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}/%plugin
install -m644 *.sample %{buildroot}%{_vdr_plugin_cfgdir}/%plugin/
mv %{buildroot}%{_vdr_plugin_cfgdir}/%plugin/vomp.conf{.sample,}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README
%dir %{_vdr_plugin_cfgdir}/%plugin
%config(noreplace) %{_vdr_plugin_cfgdir}/%plugin/vomp.conf
# sample file, thus no noreplace
%config %{_vdr_plugin_cfgdir}/%plugin/vomp-00-00-00-00-00-00.conf.sample

