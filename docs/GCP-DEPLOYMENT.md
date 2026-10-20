# ☁️ Google Cloud Platform (GCP) Deployment Guide

This guide details how to deploy **Bilota (بيلوتا / قطوة)** to **Google Cloud Run** or **Google App Engine** with automatic HTTPS, zero server management, and instant public accessibility for hackathon judges.

---

## 🌟 Recommended Target: Google Cloud Run

Google Cloud Run is the premier serverless container platform on GCP:
* **Cost:** Free tier includes 2 million requests/month (effectively \$0.00 for hackathon demos).
* **Speed:** Scales to zero when idle; cold start < 1.5 seconds.
* **Middle East Region:** Supports `me-central1` (Middle East / Doha) or `me-west1` for low latency in the UAE.
* **Security:** Runs as non-root user with automated SSL certificates and HTTPS.

---

## 🚀 Deployment Method 1: Cloud Run GitHub Integration (Fastest, 2 Minutes, Zero CLI)

No local `gcloud` or Docker installation needed.

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. In the top search bar, type **Cloud Run** and select it.
3. Click **"Create Service"** (or **"Deploy Container"**).
4. Choose **"Continuously deploy from a repository"** and click **"Set Up with Cloud Build"**.
5. Select **GitHub** as the provider:
   * Authenticate your GitHub account.
   * Repository: Select **`swaritbkp/Bilota_h2_online`**.
   * Branch: `^main$`.
   * Build Type: Select **Dockerfile** (source path: `/Dockerfile`).
6. Configure the Service:
   * **Service Name:** `bilota-app`
   * **Region:** `me-central1` (or `us-central1` / `europe-west1`)
   * **Authentication:** Select **"Allow unauthenticated invocations"** (essential so hackathon judges can open the link).
   * **Container Port:** `8080`
   * **Memory:** `512 MiB` (sufficient for production)
7. Click **"Create"**.
8. Cloud Build will automatically build the image, deploy the container, and provide your live public URL:
   ```text
   https://bilota-app-xxxxxxxxxx-me-central1.a.run.app
   ```

---

## ⚡ Deployment Method 2: Google Cloud Shell (Single Terminal Command)

If you have the GCP web console open:

1. Click the **Cloud Shell** icon (`>_`) in the top right corner of the [GCP Console](https://console.cloud.google.com/).
2. Paste the following commands:

```bash
# 1. Clone the public repository
git clone https://github.com/swaritbkp/Bilota_h2_online.git
cd Bilota_h2_online

# 2. Deploy directly from source to Cloud Run
gcloud run deploy bilota-app \
  --source . \
  --region me-central1 \
  --allow-unauthenticated \
  --port 8080
```

3. When prompted:
   * *"Do you want to enable Artifact Registry and Cloud Build?"* $\to$ Type `y` (Yes).
4. Within 90 seconds, Cloud Run outputs your live service URL.

---

## 💻 Deployment Method 3: Local `gcloud` CLI (Developer Machine)

If you install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install):

```powershell
# 1. Authenticate with your Google Cloud account
gcloud auth login

# 2. Set your active project ID
gcloud config set project YOUR_PROJECT_ID

# 3. Deploy to Cloud Run using the pre-configured Dockerfile
gcloud run deploy bilota-app `
  --source . `
  --region me-central1 `
  --allow-unauthenticated `
  --port 8080
```

---

## 🧪 Post-Deployment Verification

Once deployed, verify the public URL in an incognito window:
* **Dashboard:** `https://<YOUR-CLOUD-RUN-URL>/`
* **Health Check:** `https://<YOUR-CLOUD-RUN-URL>/api/health`
* **Inference Endpoint:** `https://<YOUR-CLOUD-RUN-URL>/api/analyze`
* **Family Majlis Oasis:** `https://<YOUR-CLOUD-RUN-URL>/api/family-oasis`
* **Sovereign QR Endpoint:** `https://<YOUR-CLOUD-RUN-URL>/api/family-qr-generate`

Update **`docs/SUBMISSION.md`** (Field 3) and **`README.md`** with your live GCP URL once deployed!
