/**
 * Marcen AI - Cliente API
 * Comunicação com o backend
 */

import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// ===== PROJETOS =====

export const createProject = async (projectData) => {
  const response = await api.post('/api/v1/projects/', projectData)
  return response.data
}

export const listProjects = async (skip = 0, limit = 50) => {
  const response = await api.get(`/api/v1/projects/?skip=${skip}&limit=${limit}`)
  return response.data
}

export const getProject = async (projectId) => {
  const response = await api.get(`/api/v1/projects/${projectId}`)
  return response.data
}

export const refineProject = async (projectId, refinementNotes) => {
  const response = await api.post(`/api/v1/projects/${projectId}/refine`, {
    refinement_notes: refinementNotes
  })
  return response.data
}

export const deleteProject = async (projectId) => {
  const response = await api.delete(`/api/v1/projects/${projectId}`)
  return response.data
}

export const selectImage = async (projectId, imageId) => {
  const response = await api.patch(`/api/v1/projects/${projectId}/images/${imageId}/select`)
  return response.data
}

// ===== HEALTH =====

export const healthCheck = async () => {
  const response = await api.get('/health')
  return response.data
}

export default api
