"use client";

import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import { toast } from "sonner";

const CloudConnect: React.FC = () => {
  const [status, setStatus] = useState("");

  const handleOAuthConnect = async (provider: string) => {
    try {
      setStatus(`Connecting to ${provider}...`);

      // Optional: Redirect to OAuth URL or open popup
      const res = await fetch("/api/cloud-connect", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ provider })
      });

      const data = await res.json();
      if (res.ok) {
        toast.success(`${provider} connection initiated!`);
        setStatus(`${provider} integration successful.`);
      } else {
        toast.error(data.error || "Connection failed.");
        setStatus("Error occurred.");
      }
    } catch (err) {
      toast.error("Something went wrong.");
      setStatus("Failed to connect.");
    }
  };

  return (
    <div className="p-6 space-y-4 max-w-xl mx-auto">
      <h2 className="text-2xl font-semibold">🔐 Connect Cloud Provider</h2>

      <Button variant="outline" onClick={() => handleOAuthConnect("aws")}>
        Connect to AWS
      </Button>
      <Button variant="outline" onClick={() => handleOAuthConnect("azure")}>
        Connect to Azure
      </Button>
      <Button variant="outline" onClick={() => handleOAuthConnect("gcp")}>
        Connect to GCP
      </Button>

      <p className="text-gray-600">{status}</p>
    </div>
  );
};

export default CloudConnect;
