# ビジネス法務検定3級 毎日学習サイト起動スクリプト

Write-Host "========================================"
Write-Host "ビジネス法務検定3級 毎日学習サイト" -ForegroundColor Cyan
Write-Host "========================================"
Write-Host ""

# スクリプトのディレクトリに移動
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath
Write-Host "現在のディレクトリ: $PWD"
Write-Host ""

# Pythonの確認
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python確認: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "エラー: Pythonがインストールされていません。" -ForegroundColor Red
    Write-Host "Pythonをインストールしてから再実行してください。"
    Read-Host "Enterキーを押して終了"
    exit 1
}

# ポート8080の確認
Write-Host "ポート8080の使用状況を確認中..."
$portInUse = Get-NetTCPConnection -LocalPort 8080 -ErrorAction SilentlyContinue
if ($portInUse) {
    Write-Host ""
    Write-Host "警告: ポート8080は既に使用されています。" -ForegroundColor Yellow
    $continue = Read-Host "続行しますか？ (Y/N)"
    if ($continue -ne 'Y' -and $continue -ne 'y') {
        exit 1
    }
}

# サーバー起動
Write-Host ""
Write-Host "ローカルサーバーを起動します..." -ForegroundColor Green

# 新しいPowerShellウィンドウでサーバーを起動
$serverScript = @"
Write-Host 'Bizlaw Server - ポート8080で起動中...' -ForegroundColor Cyan
Write-Host 'サーバーを停止するには Ctrl+C を押してください'
Write-Host ''
python -m http.server 8080
"@

$tempFile = [System.IO.Path]::GetTempFileName() + ".ps1"
$serverScript | Out-File -FilePath $tempFile -Encoding UTF8

Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy Bypass", "-File `"$tempFile`""

# サーバーの起動を待つ
Write-Host "サーバーの起動を待っています..."
Start-Sleep -Seconds 3

# ブラウザで開く
Write-Host ""
Write-Host "ブラウザでサイトを開きます..." -ForegroundColor Green
Start-Process "http://localhost:8080"

Write-Host ""
Write-Host "========================================"
Write-Host "サーバーが起動しました！" -ForegroundColor Green
Write-Host "URL: http://localhost:8080" -ForegroundColor Cyan
Write-Host ""
Write-Host "サーバーを停止するには:"
Write-Host "1. サーバーウィンドウで Ctrl+C を押す"
Write-Host "2. または、ウィンドウを閉じる"
Write-Host "========================================"
Write-Host ""
Write-Host "このウィンドウは閉じても構いません。"
Read-Host "Enterキーを押して終了"
