import React from 'react';
import { StyleSheet, View, Text, ScrollView, TouchableOpacity } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const DashboardScreen = ({ navigation }) => {
  // Placeholder data for dashboard
  const stats = [
    { id: '1', title: 'Plants Identified', count: 24, icon: 'leaf' },
    { id: '2', title: 'Questions Asked', count: 56, icon: 'chatbubble-ellipses' },
    { id: '3', title: 'Research Queries', count: 12, icon: 'document-text' },
  ];

  const recentSessions = [
    { id: '1', title: 'Yellow leaves on tomato plant', date: '2 hours ago', type: 'plant' },
    { id: '2', title: 'Soil pH for blueberries', date: '1 day ago', type: 'soil' },
    { id: '3', title: 'Sustainable farming practices', date: '3 days ago', type: 'research' },
  ];

  const renderStatCard = ({ id, title, count, icon }) => (
    <View key={id} style={styles.statCard}>
      <Ionicons name={icon} size={32} color="#2e7d32" />
      <Text style={styles.statCount}>{count}</Text>
      <Text style={styles.statTitle}>{title}</Text>
    </View>
  );

  const renderSessionItem = ({ id, title, date, type }) => {
    let iconName = 'leaf';
    if (type === 'soil') iconName = 'flask';
    if (type === 'research') iconName = 'document-text';

    return (
      <TouchableOpacity 
        key={id} 
        style={styles.sessionItem}
        onPress={() => navigation.navigate('Chat')}
      >
        <View style={styles.sessionIcon}>
          <Ionicons name={iconName} size={24} color="#2e7d32" />
        </View>
        <View style={styles.sessionInfo}>
          <Text style={styles.sessionTitle}>{title}</Text>
          <Text style={styles.sessionDate}>{date}</Text>
        </View>
        <Ionicons name="chevron-forward" size={20} color="#888" />
      </TouchableOpacity>
    );
  };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Your Ecological Journey</Text>
        <Text style={styles.headerSubtitle}>Track your progress and insights</Text>
      </View>

      <View style={styles.statsContainer}>
        {stats.map(renderStatCard)}
      </View>

      <View style={styles.sectionContainer}>
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Recent Sessions</Text>
          <TouchableOpacity onPress={() => {}}>
            <Text style={styles.seeAllText}>See All</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.sessionsList}>
          {recentSessions.map(renderSessionItem)}
        </View>
      </View>

      <View style={styles.sectionContainer}>
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Ecological Tips</Text>
        </View>
        <View style={styles.tipCard}>
          <Ionicons name="bulb" size={24} color="#2e7d32" style={styles.tipIcon} />
          <Text style={styles.tipText}>
            Water your plants in the early morning or evening to reduce evaporation and make the most of your water.
          </Text>
        </View>
      </View>

      <TouchableOpacity 
        style={styles.newChatButton}
        onPress={() => navigation.navigate('Chat')}
      >
        <Ionicons name="chatbubble" size={20} color="#fff" />
        <Text style={styles.newChatButtonText}>New Chat</Text>
      </TouchableOpacity>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    padding: 20,
    backgroundColor: '#2e7d32',
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 5,
  },
  headerSubtitle: {
    fontSize: 16,
    color: '#e0e0e0',
  },
  statsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    padding: 15,
    marginTop: -30,
  },
  statCard: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 15,
    alignItems: 'center',
    width: '31%',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  statCount: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginTop: 5,
  },
  statTitle: {
    fontSize: 12,
    color: '#666',
    textAlign: 'center',
    marginTop: 5,
  },
  sectionContainer: {
    backgroundColor: '#fff',
    borderRadius: 10,
    margin: 15,
    marginTop: 10,
    padding: 15,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  sectionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 15,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#333',
  },
  seeAllText: {
    fontSize: 14,
    color: '#2e7d32',
    fontWeight: '500',
  },
  sessionsList: {
    marginBottom: 5,
  },
  sessionItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#f0f0f0',
  },
  sessionIcon: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: '#e8f5e9',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 15,
  },
  sessionInfo: {
    flex: 1,
  },
  sessionTitle: {
    fontSize: 16,
    color: '#333',
    marginBottom: 3,
  },
  sessionDate: {
    fontSize: 12,
    color: '#888',
  },
  tipCard: {
    backgroundColor: '#e8f5e9',
    borderRadius: 8,
    padding: 15,
    flexDirection: 'row',
    alignItems: 'flex-start',
  },
  tipIcon: {
    marginRight: 10,
    marginTop: 2,
  },
  tipText: {
    flex: 1,
    fontSize: 14,
    color: '#333',
    lineHeight: 20,
  },
  newChatButton: {
    backgroundColor: '#2e7d32',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 15,
    borderRadius: 30,
    margin: 15,
    marginTop: 5,
  },
  newChatButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
    marginLeft: 8,
  },
});

export default DashboardScreen;