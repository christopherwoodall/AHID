
#https://docs.microsoft.com/en-us/uwp/api/Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager?view=winrt-22000
#https://superuser.com/questions/1341997/using-a-uwp-api-namespace-in-powershell/1342416#1342416


########################################################
# https://stackoverflow.com/questions/45833873/enable-windows-10-built-in-hotspot-by-cmd-batch-powershell

$connectionProfile = [Windows.Networking.Connectivity.NetworkInformation,Windows.Networking.Connectivity,ContentType=WindowsRuntime]::GetInternetConnectionProfile()
$tetheringManager = [Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager,Windows.Networking.NetworkOperators,ContentType=WindowsRuntime]::CreateFromConnectionProfile($connectionProfile)

# Be sure to include Ben N.'s await for IAsyncOperation:
# https://superuser.com/questions/1341997/using-a-uwp-api-namespace-in-powershell

# Check whether Mobile Hotspot is enabled
$tetheringManager.TetheringOperationalState

# Start Mobile Hotspot
Await ($tetheringManager.StartTetheringAsync()) ([Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult])

# Stop Mobile Hotspot
Await ($tetheringManager.StopTetheringAsync()) ([Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult])

####################################################

[Windows.System.UserProfile.LockScreen,Windows.System.UserProfile,ContentType=WindowsRuntime] | Out-Null
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | ? { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]
Function Await($WinRtTask, $ResultType) {
    $asTask = $asTaskGeneric.MakeGenericMethod($ResultType)
    $netTask = $asTask.Invoke($null, @($WinRtTask))
    $netTask.Wait(-1) | Out-Null
    $netTask.Result
}
Function AwaitAction($WinRtAction) {
    $asTask = ([System.WindowsRuntimeSystemExtensions].GetMethods() | ? { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and !$_.IsGenericMethod })[0]
    $netTask = $asTask.Invoke($null, @($WinRtAction))
    $netTask.Wait(-1) | Out-Null
}
$connectionProfile = [Windows.Networking.Connectivity.NetworkInformation,Windows.Networking.Connectivity,ContentType=WindowsRuntime]::GetInternetConnectionProfile()
$tetheringManager = [Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager,Windows.Networking.NetworkOperators,ContentType=WindowsRuntime]::CreateFromConnectionProfile($connectionProfile)

# Be sure to include Ben N.'s await for IAsyncOperation:
# https://superuser.com/questions/1341997/using-a-uwp-api-namespace-in-powershell

# Check whether Mobile Hotspot is enabled
$tetheringManager.TetheringOperationalState

# Start Mobile Hotspot
Await ($tetheringManager.StartTetheringAsync()) ([Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult])